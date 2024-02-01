from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseNotAllowed


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # Authentication successful
            return JsonResponse({'success': True})
        else:
            # Authentication failed
            return JsonResponse({'success': False, 'error': 'Invalid Credentials'}, status=401)
    else:
        # Return an error response for GET requests
        return HttpResponseNotAllowed(['POST'], 'Only POST requests are allowed for login.')

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         # Authenticate user
#         user = authenticate(username=username, password=password)
        
#         if user is not None:
#             # Authentication successfull
#             return JsonResponse({'success': True})
#         else:
#             # Authentication failed
#             return JsonResponse({'success': False, 'error': 'Invalid Credentials'}, status=401)

def register(request):
    if request.method == 'POST':
        print(JsonResponse)
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        # Check if the username or email is already in use
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)
        
        # Create a new user
        user = User.objects.create_user(username, email, password)
        
        # Optionally, you can perform additional actions like sending a confirmation email
        
        return JsonResponse({'message': 'User registered successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
