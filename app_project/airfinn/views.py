from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .models import Item, User
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings # Import settings to get the frontend URL
from fernet import Fernet
import json
import jwt
from airfinn.utils import get_user_by_id, email_checks, password_checks



def index(request):
    return JsonResponse({'message': 'Welcome to Airfinn!'})

def get_user_id_for_token_auth(request):
    """
    Pull the token from the request cookies and decode it to get the user info from the database. 
    Return a JsonResponse object with the user id. 
    """
    # Pull token from request cookies and decode it to get the user info
    token = request.COOKIES.get('token')
    # Decode the token
    secret_key = 'St3rkP@ssord'
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        user_id = payload['user_id']
        return user_id
    
    except Exception as e:
        return None


"""
Pull the token from the request cookies and decode it to get the user info from the database. 
Return a JsonResponse object with the user info. 
(name and email as of now, should be extended to include more info: phone number, address, etc.)
"""
def dashboard(request):

    # Pull token from request cookies and decode it to get the user info
    token = request.COOKIES.get('token')
    # Decode the token
    secret_key = 'St3rkP@ssord'
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        user_id = payload['user_id']
    except jwt.ExpiredSignatureError:
        return JsonResponse({'error': 'Token has expired'}, status=401)
    except jwt.InvalidTokenError:
        return JsonResponse({'error': 'Invalid token'}, status=401)

    # Get the user from the database
    user = get_user_by_id(user_id)
    print(user)
    print("usertype: ", type(user))

    if type(user) != type(User): 
        JsonResponse({'success': False, 'error': 'User does not exist'}, status=401)

    return JsonResponse({'email': user.email, 'firstName': user.first_name, 'lastName': user.last_name, 'address': user.address, 'phone': user.phone, 'verified': user.is_verified})

"""
Function to logout the user by clearing the token cookie and setting the auth_user cookie to False. 
This function returns a JsonResponse object with the cookies set to expire immediately.
The result is that the token is invalidated and the user cant access the dashboard until the user logs in again.
"""

def logout(request):
    # Create a response object with an empty dictionary or a simple message
    response = JsonResponse({'message': 'Logged out successfully'}, safe=False)
    
    # Clear all cookies by setting their expiration time to a past date
    response.set_cookie('token', '', expires=0)
    
    return response
"""
Function to login the user and set the token as a cookie in the response.
This function returns a JsonResponse object with the token set as a cookie.
The result is that the user can access the dashboard until the token expires.
"""
    
def login(request):
    # Check if the request method is POST
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed for login.'}, status=405)
    
    # Process the decrypted payload
    data = json.loads(request.body)

    # Encrypt the password
    key = Fernet.generate_key()
    fernet =  Fernet(key)
    encrypted_password = fernet.encrypt(data.get('password').encode())

    pword = fernet.decrypt(encrypted_password).decode()
    print(f"data.get.password: {data.get('password')}, data.get.username: {data.get('username')}")
    # Authenticate user
    user = authenticate(request, username=data.get('username'), password=data.get('password'))
    
    # Authentication successful
    if user:
        # Generate an access token
        secret_key = 'St3rkP@ssord' 
        token = jwt.encode({'user_id': user.id}, secret_key, algorithm='HS256')
        
        # Set the token as a cookie in the response
        response = JsonResponse({'token': token})
        # Set the auth_user cookie to True    
        response.set_cookie('token', token, httponly=False, secure=False, samesite=False)

        # Return the response
        return response
    
    else:
        # Authentication failed
        return JsonResponse({'success': False, 'error': 'Invalid Credentials'}, status=401)
    
"""
Function to register the user and set the token as a cookie in the response.
This function returns a JsonResponse object with the token set as a cookie.
The result is that the user can access the dashboard until the token expires,
and they have created a user which is stored in the database.
"""
def register(request):
    # Check if the request method is POST
    if request.method != 'POST':
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

    # Get JSON data from the request body
    data = json.loads(request.body)
    # get username and encrypt password and email.

    # Check if the email, password and username is empty
    if data.get('email') == '': 
        return JsonResponse({'error_email': 'Requires email to register an account'}, status=400)
    if data.get('password1') == '':
        return JsonResponse({'error_password': 'Requires password to register an account'}, status=400)
    if data.get('password2') == '':
        return JsonResponse({'error_password': 'Requires password to register an account'}, status=400)
    if data.get('username') == '':
        return JsonResponse({'error_username': 'Requires username to register an account'}, status=400)

    # Encrypt the password 
    key = Fernet.generate_key()
    fernet =  Fernet(key)
    encrypted_password1 = fernet.encrypt(data.get('password1').encode())
    encrypted_password2 = fernet.encrypt(data.get('password2').encode())

    # Check if the password and email is valid
    if password_checks(fernet.decrypt(encrypted_password1).decode()) == False:
        return password_checks(fernet.decrypt(encrypted_password1).decode())
    if password_checks(fernet.decrypt(encrypted_password2).decode()) == False:
        return password_checks(fernet.decrypt(encrypted_password1).decode())

    # Check if the passwords match
    elif fernet.decrypt(encrypted_password1).decode() != fernet.decrypt(encrypted_password2).decode():
        return JsonResponse({'error': 'Passwords do not match'}, status=400)

    # Encrypt the email
    enc_email = fernet.encrypt(data.get('email').encode())
    if email_checks(fernet.decrypt(enc_email).decode()) == False:
        return email_checks(fernet.decrypt(enc_email).decode())
        
    # Check if the username or email is already in use
    if User.objects.filter(email=data.get('email')).exists():
        return JsonResponse({'error': 'Email already exists'}, status=400)
    
    username = fernet.decrypt(enc_email).decode()
    # Create a new user
    user = User.objects.create_user(username= fernet.decrypt(enc_email).decode(), 
                                    email= fernet.decrypt(enc_email).decode(), 
                                    password= fernet.decrypt(encrypted_password1).decode(),
                                    first_name= data.get('firstName'),
                                    last_name= data.get('lastName'),
                                    address= data.get('address'),
                                    phone=data.get('phone')
                                    )

    # Create cookie token to direct user to dashboard
    if user is not None:
        # Authentication successful
        # Generate an access token
        secret_key = 'St3rkP@ssord' 
        token = jwt.encode({'user_id': user.id}, secret_key, algorithm='HS256')
        
        # Set the token as a cookie in the response
        response = JsonResponse({'token': token})
        response.set_cookie('token', token, httponly=False, secure=False, samesite=False)
        print(response.cookies)
        
        verification_token = jwt.encode({'user_id': user.id}, settings.SECRET_KEY, algorithm='HS256')
        
        verification_link = f"{settings.FRONTEND_URL}/verify-email?token={verification_token}"
        
        # Load HTML content from template
        html_content = render_to_string('verification_email.html', {'verification_link': verification_link, 'username': username})
    
        # Load plain text content from template
        text_content = render_to_string('verification_email.txt', {'verification_link': verification_link, 'username': username})

        # Create EmailMultiAlternatives object to include both versions
        subject = "Verify Your Email"
        from_email = "noreply@dybedahlserver.net"
        to_email = fernet.decrypt(enc_email).decode()
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, "text/html")
        
        # Set the token as a cookie in the response
        response = JsonResponse({'token': token, 'auth_user': True, 'verification_sent': True})
        response.set_cookie('token', token, httponly=False, secure=False, samesite=False)
        
        # Send the email
        msg.send()
        
        return response
    else:
        # Authentication failed
        return JsonResponse({'success': False, 'error': 'Not able to create user'}, status=401)

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
        
        # Get the frontend URL from settings or pass it as a parameter
        frontend_url = settings.FRONTEND_URL  # Assuming you set FRONTEND_URL in your settings
        
        # Construct the reset link with the correct frontend URL
        reset_link = f"{frontend_url}/reset-password/{uidb64}/{token}/"
        
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
    
def verify_email(request):    
    token = request.GET.get('token')

    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_id = decoded_token.get('user_id')
        
        user = User.objects.get(id=user_id)
        user.is_verified = True
        user.save()

        return JsonResponse({'message': 'Email verified successfully'}, status=200)
    except jwt.ExpiredSignatureError:
        return JsonResponse({'message': 'Verification link has expired'}, status=400)
    except jwt.DecodeError:
        return JsonResponse({'message': 'Invalid verification token'}, status=400)
 
def search_items(request):
    query = request.GET.get('q', '')
    if query:
        items = Item.objects.filter(name__icontains=query)
    else:
        items = Item.objects.all()
    data = [{'id': item.id, 'name': item.name} for item in items]
    return JsonResponse(data, safe=False)

def delete_listing(request, item_id):
    """
    Function to delete an existing listing
    ID is the primary key of the item.
    """
    try:
        if request.method != 'DELETE':
            return JsonResponse({'error': 'Method Not Allowed'}, status=405)
        
        item = Item.objects.get(id=item_id)
        # user_token_id = get_user_id_for_token_auth(request)

                    
        item.delete()
        return JsonResponse({'message': 'Listing deleted successfully'}, status = 200)
    
    
    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item does not exist'}, status=404)