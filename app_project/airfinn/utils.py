from .models import Item, User, Order
from django.http import JsonResponse, HttpResponseNotAllowed
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
import re
import json
from django.contrib.auth import get_user_model
from datetime import datetime
from django.db.models import Q

def get_user_by_id(user_id):
    User = get_user_model()  # Get the custom user model
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


def email_checks(email):
    # Check if the email is valid
    if not re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return JsonResponse({'error': 'Invalid email address'}, status=400)
    return True


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
    if is_simple_sequence(password):
        return JsonResponse({'error': 'Password can not be a sequence of numbers'}, status=400)

    return True

def upload_profile_picture(request):
    print('upload_profile_picture')
    if request.method == 'POST' :
        print('in if')
        profile_picture = request.FILES['profilePicture']
            
        # Process the uploaded image here
        # For example, you can save the image to a specific location or perform additional operations
            
        return JsonResponse({'message': 'Profile picture uploaded successfully'})
    else:
         print('in else')
         return JsonResponse({'error': 'Failed to upload profile picture'}, status=400)


def get_reserved_items(user):
    order = Order.objects.filter(renter_id=user)
    items = [order.item for order in order]
    data = serialize('json', items)

    return data

def is_item_available(item, start_date, end_date):
    # Ensure input dates are datetime objects
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Query to check for any overlapping orders
    # First use the Q objects combined by the '&' operator inside the filter method
    orders = Order.objects.filter(
        Q(end_date__gte=start_date) & Q(start_date__lte=end_date),
        item=item  # Make sure 'item' comes after the Q objects
    )
    return not orders.exists()  # Returns True if no overlapping orders found