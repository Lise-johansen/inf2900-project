from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, AnonymousUser
from django.http import JsonResponse, HttpResponseNotAllowed
from cryptography.fernet import Fernet
import json
import jwt
import re



def get_user_by_id(user_id):
    try:
        user = User.objects.get(id=user_id)
        return user
    except User.DoesNotExist:
        return None

def is_simple_sequence(password, length=4):
    # Check if the password is composed of a sequence of digits
    for i in range(len(password) - length + 1):
        sequence = password[i:i+length]
        if sequence.isdigit() and sequence == ''.join(str(int(sequence[0]) + i) for i in range(length)):
            return True
    return False

    
def password_checks(password):
    if len(password) < 8:
        return JsonResponse({'error': 'Password is too short'}, status=400)
    # Check if the password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return JsonResponse({'error': 'Password should contain at least one uppercase letter'}, status=400)
    # Check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return JsonResponse({'error': 'Password should contain at least one lowercase letter'}, status=400)
    # Check if the password contains at least one digit
    if not re.search(r'\d', password):
        return JsonResponse({'error': 'Password should contain at least one number'}, status=400)
    # Check if the password contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return JsonResponse({'error': 'Password should contain at least one special character'}, status=400)
    
    # Check if the password is not based on common patterns or sequences
    # Additional checks if needed
    has_alpha = any(c.isalpha() for c in password)
    has_special = any(c in "!@#$%^&*(),.?\":{}|<>" for c in password)

    if is_simple_sequence(password):
        return JsonResponse({'error': 'Password can not be a sequence of numbers'}, status=400)

    return True



    

def index(request):
    return JsonResponse({'message': 'Welcome to Airfinn!'})

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
    


def login(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed for login.'}, status=405)
    
    # Process the decrypted payload
    data = json.loads(request.body)
    username = data.get('username')

    key = Fernet.generate_key()
    fernet =  Fernet(key)
    encrypted_password = fernet.encrypt(data.get('password').encode())
    print("encrypted pw: ",encrypted_password)
    print("pulled pw: ", data.get('password'))
    
    # Authenticate user
    user = authenticate(request, username=username, password=fernet.decrypt(encrypted_password).decode())
        
    if user is not None:
        # Authentication successful
        # Generate an access token
        secret_key = 'St3rkP@ssord' 
        token = jwt.encode({'user_id': user.id}, secret_key, algorithm='HS256')
        
        # Set the token as a cookie in the response
        response = JsonResponse({'token': token})
        response.set_cookie('token', token, httponly=False, secure=False, samesite=False)
        
        return response
    
    else:
        # Authentication failed
        return JsonResponse({'success': False, 'error': 'Invalid Credentials'}, status=401)
    

def register(request):

    if request.method != 'POST':
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

    # Get JSON data from the request body
    data = json.loads(request.body)
    # get username and encrypt password and email.
    username = data.get('username')

    if data.get('email') == '': 
        return JsonResponse({'error_email': 'Requires email to register an account'}, status=400)

    key = Fernet.generate_key()
    fernet =  Fernet(key)
    encrypted_password = fernet.encrypt(data.get('password').encode())

    if password_checks(fernet.decrypt(encrypted_password).decode()) == True:
        print("okay password")
    else:
        return password_checks(fernet.decrypt(encrypted_password).decode())


    enc_email = fernet.encrypt(data.get('email').encode())
        
    # Check if the username or email is already in use
    if User.objects.filter(username=username).exists():
        return JsonResponse({'error_username_exists': 'Username already exists'}, status=400)
    if User.objects.filter(email=fernet.decrypt(enc_email).decode()).exists():
        return JsonResponse({'error_email_exists': 'Email already exists'}, status=400)
        
    # Create a new user
    user = User.objects.create_user(username, fernet.decrypt(enc_email).decode(), fernet.decrypt(encrypted_password).decode())
    # Optionally, you can perform additional actions like sending a confirmation email
        
    # Create cookie token to direct user to dashboard
    if user is not None:
        # Authentication successful
        # Generate an access token
        secret_key = 'St3rkP@ssord' 
        token = jwt.encode({'user_id': user.id}, secret_key, algorithm='HS256')
        
        # Set the token as a cookie in the response
        response = JsonResponse({'token': token})
        response.set_cookie('token', token, httponly=False, secure=False, samesite=False)
        
        return response
    else:
        # Authentication failed
        return JsonResponse({'success': False, 'error': 'Not able to create user'}, status=401)
    