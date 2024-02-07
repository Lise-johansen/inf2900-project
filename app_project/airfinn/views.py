from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
import json





def index(request):
    return render(request, 'index.html')

def dashboard(request):

    if request.user.is_authenticated:
        return JsonResponse({'message': 'You are authenticated'}, status=200)

@csrf_exempt
def login(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'], 'Only POST requests are allowed for login.')
    

    # Process the decrypted payload
    data = json.loads(request.body)

    username = data.get('username')
    password = data.get('password')
        
    # Authenticate user
    user = authenticate(username=username, password=password)
        
    if user is not None:
        # Authentication successful
        return JsonResponse({'success': True})
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


@csrf_exempt
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
