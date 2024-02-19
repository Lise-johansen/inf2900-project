from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.models import User, AnonymousUser
from django.http import JsonResponse, HttpResponseNotAllowed
from cryptography.fernet import Fernet
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
import json
import jwt
from airfinn.utils import get_user_by_id, email_checks, password_checks, search_items


def index(request):
    return JsonResponse({'message': 'Welcome to Airfinn!'})

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

    return JsonResponse({'username': user.username, 'email': user.email})

"""
Function to logout the user by clearing the token cookie and setting the auth_user cookie to False. 
This function returns a JsonResponse object with the cookies set to expire immediately.
The result is that the token is invalidated and the user cant access the dashboard until the user logs in again.
"""
def logout(request):
    # Create a response object
    response = JsonResponse()
    # Clear all cookies by setting their expiration time to a past date
    response.set_cookie('token', '', expires=0)
    response.set_cookie('auth_user', False)
    
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
    username = data.get('username')

    # Encrypt the password
    key = Fernet.generate_key()
    fernet =  Fernet(key)
    encrypted_password = fernet.encrypt(data.get('password').encode())


    # Authenticate user
    user = authenticate(request, username=username, password=fernet.decrypt(encrypted_password).decode())
        
    # Authentication successful
    if user is not None:
        # Generate an access token
        secret_key = 'St3rkP@ssord' 
        token = jwt.encode({'user_id': user.id}, secret_key, algorithm='HS256')
        
        # Set the token as a cookie in the response
        response = JsonResponse({'token': token, 'auth_user': True})
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
    username = data.get('username')

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
    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'Username already exists'}, status=400)
    if User.objects.filter(email=fernet.decrypt(enc_email).decode()).exists():
        return JsonResponse({'error': 'Email already exists'}, status=400)
        
    # Create a new user
    user = User.objects.create_user(username, fernet.decrypt(enc_email).decode(), fernet.decrypt(encrypted_password1).decode())

    # Create cookie token to direct user to dashboard
    if user is not None:
        # Authentication successful
        # Generate an access token
        secret_key = 'St3rkP@ssord' 
        token = jwt.encode({'user_id': user.id}, secret_key, algorithm='HS256')
        
        # Set the token as a cookie in the response
        response = JsonResponse({'token': token, 'auth_user': True})
        response.set_cookie('token', token, httponly=False, secure=False, samesite=False)
        
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
        token_generator = PasswordResetTokenGenerator()
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)
        reset_link = f"http://localhost:8080/reset-password/{uidb64}/{token}/"
        
        # Load HTML content from template
        html_content = render_to_string('password_reset_email.html', {'reset_link': reset_link})
        
        # Load plain text content from template
        text_content = render_to_string('password_reset_email.txt', {'reset_link': reset_link})
        
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
        return JsonResponse({'error': 'User not found'}, status=404)



def userregister(response):
    print('UserRegister')
    return JsonResponse({'message': 'User registered successfully!'})