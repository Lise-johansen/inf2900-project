from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, AnonymousUser
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
import json
import jwt

def user_data(request):

    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Get the current authenticated user
        user = request.user

        # Serialize the user data (you can customize this as needed)
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
            # Add any other user data you want to include
        }

        # Return the user data as JSON response
        return JsonResponse(user_data)
    else:
        # If the user is not authenticated, return an error response
        return JsonResponse({'error': 'User is not authenticated'}, status=401)

def index(request):
    return render(request, 'index.html')

def dashboard(request):

    # Pull token from request cookies and decode it to get the user_id
    token = request.COOKIES.get('token')
    # Decode the token
    secret_key = 'St3rkP@ssord'
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        user_id = payload.get('user_id')
    except jwt.ExpiredSignatureError:
        return JsonResponse({'error': 'Token has expired'}, status=401)
    except jwt.InvalidTokenError:
        return JsonResponse({'error': 'Invalid token'}, status=401)
    # Get the user from the database
    user = get_object_or_404(User, pk=user_id)

    return JsonResponse({'username': user.username, 'email': user.email})
    

def login(request):
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
        payload = {'user_id': user.id}
        secret_key = 'St3rkP@ssord'  # Replace with your own secret key
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        
        response_data = {
            'success': True,
            'token': token,  # Return token directly
            'message': 'User authenticated successfully.',
            'user_auth': True,
        }
        return JsonResponse(response_data)
    else:
        # Authentication failed
        return JsonResponse({'success': False, 'error': 'Invalid Credentials'}, status=401)
# @csrf_exempt
# def login(request):
#     print(f"request: ",request.method)
#     if request.method != 'POST':
#         return JsonResponse({'error': 'Method Not Allowed'}, status=405)

#     # Get the encrypted payload from the request body
#     encrypted_payload = request.POST.get('encryptedPayload')

#     # Decrypt the payload using RSA private key
#     key = RSA()
#     key.importKey(open('private.pem').read())  # Import RSA private key from file
#     decrypted_data = key.decrypt(encrypted_payload, 'utf8')

#     # Parse JSON data from the decrypted payload
#     user_data = json.loads(decrypted_data)
#     print(f"user_data: ",user_data)
        
#     username = user_data.get('username')
#     password = user_data.get('password')
        
#     # Authenticate user
#     user = authenticate(username=username, password=password)
        
#     if user is not None:
#         # Authentication successful
#         return JsonResponse({'success': True})
#     else:
#         # Authentication failed
#         return JsonResponse({'success': False, 'error': 'Invalid Credentials'}, status=401)



def register(request):
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
