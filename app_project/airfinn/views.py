from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.models import User, AnonymousUser
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .models import Item 
import json
import jwt

def get_user_by_id(user_id):
    try:
        user = User.objects.get(id=user_id)
        return user
    except User.DoesNotExist:
        return None

def index(request):
    return JsonResponse({'message': 'Welcome to Airfinn!'})

def dashboard(request):
    print("request: ",request)
    print("request.method: ",request.method)
    print("request.body: ",request.body)
    print("request.COOKIES: ",request.COOKIES)

    print("Working in dashboard function")

    # Pull token from request cookies and decode it to get the user info
    token = request.COOKIES.get('token')
    print("dashboard token: ",token)
    # Decode the token
    secret_key = 'St3rkP@ssord'
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        user_id = payload['user_id']
    except jwt.ExpiredSignatureError:
        return JsonResponse({'error': 'Token has expired'}, status=401)
    except jwt.InvalidTokenError:
        return JsonResponse({'error': 'Invalid token'}, status=401)
    print("we move on")
    # Get the user from the database
    user = get_user_by_id(user_id)
    print("user: ",user)

    print("returning user: ",user)

    return JsonResponse({'username': user.username, 'email': user.email})
    
def login(request, user=None):
    print("Working in login function")
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed for login.'}, status=405)
    
    # Process the decrypted payload
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    
        
    # Authenticate user
    user = authenticate(request, username=username, password=password)
        
    if user is not None:
        # Authentication successful
        # Generate an access token
        secret_key = 'St3rkP@ssord' 
        token = jwt.encode({'user_id': user.id}, secret_key, algorithm='HS256')
        print("login token: ",token)
        
        # Set the token as a cookie in the response
        response = JsonResponse({'token': token})
        response.set_cookie('token', token, httponly=False, secure=False, samesite=False)
        print("login response: ",response)
        
        return response
    
    else:
        # Authentication failed
        return JsonResponse({'success': False, 'error': 'Invalid Credentials'}, status=401)
    

def register(request):
    print("Working in register function")

    if request.method != 'POST':
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

    # Get JSON data from the request body
    data = json.loads(request.body)
        
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
        
    # Check if the username or email is already in use
    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'Username already exists'}, status=400)
    if User.objects.filter(email=email).exists():
        return JsonResponse({'error': 'Email already exists'}, status=400)
        
    # Create a new user
    user = User.objects.create_user(username, email, password)
        
    # Optionally, you can perform additional actions like sending a confirmation email
        
    return JsonResponse({'message': 'User registered successfully'}, status=201)

def send_password_reset_email(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
        
    data = json.loads(request.body)
    email = data.get('email')
    user = User.objects.filter(email=email).first()
    
    if user:
        username = user.username
        token_generator = PasswordResetTokenGenerator()
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)
        reset_link = f"https://django.dybedahlserver.net/reset-password/{uidb64}/{token}/"
        
        # Load HTML content from template
        html_content = render_to_string('password_reset_email.html', {'reset_link': reset_link, 'username': username})
        
        # Load plain text content from template
        text_content = render_to_string('password_reset_email.txt', {'reset_link': reset_link, 'username': username})
        
        # Create EmailMultiAlternatives object to include both versions
        subject = "Password Reset"
        from_email = "noreply@dybedahlserver.net"
        to_email = email
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, "text/html")
        
        # Send the email
        msg.send()
        
        return JsonResponse({'message': 'Password reset email sent'}, status=200)
    else:
        # Return a custom error message instead of raising a 404 error
        return JsonResponse({'error': 'User not found'}, status=400)
    
def reset_password(request, uidb64, token):
    if request.method == 'POST':
        # Decode uidb64 to get the user's ID
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        # Validate the token
        token_generator = PasswordResetTokenGenerator()
        if user is not None and token_generator.check_token(user, token):
            # Token is valid, process the password reset form
            form = SetPasswordForm(user=user, data=json.loads(request.body))
            if form.is_valid():
                # Update user's password in the database
                form.save()
                
                # Log the user in after password reset
                user = authenticate(request, username=user.username, password=form.cleaned_data['new_password1'])
                login(request, user)
                
                # Generate an access token
                secret_key = 'St3rkP@ssord'  # Replace with your secret key
                access_token = jwt.encode({'user_id': user.id}, secret_key, algorithm='HS256')
                
                return JsonResponse({'message': 'Password reset successfully', 'token': access_token})
            else:
                # Form is invalid, return form errors
                return JsonResponse({'error': form.errors}, status=400)
        else:
            # Invalid token or user not found, return an error response
            return JsonResponse({'error': 'Invalid password reset link'}, status=400)
    else:
        # Only POST requests are allowed for password reset
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
    
def search_items(request):
    query = request.GET.get('q', '')
    if query:
        items = Item.objects.filter(name__icontains=query)
    else:
        items = Item.objects.all()
    data = [{'id': item.id, 'name': item.name} for item in items]
    return JsonResponse(data, safe=False)