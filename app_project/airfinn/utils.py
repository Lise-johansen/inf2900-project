from .models import Item, User, Order
from django.http import JsonResponse, HttpResponseNotAllowed
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMultiAlternatives
from fernet import Fernet
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

def get_user_orders(user):
    # Get all the orders for the given user
    orders = Order.objects.filter(renter_id=user)
    data = serialize('json', orders)

    reservation_data = []
    for order in orders:
        item = Item.objects.get(id=order.item_id)
        reservation_data.append({
            'id': item.id,
            'name': item.name,
            'start_date': order.start_date,
            'end_date': order.end_date,
        })

    return reservation_data

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

def send_order_email_notification(order):
    # Send an email notification to the owner that a new order has been placed
    # Get the listing from listing id
    listing = get_object_or_404(Item, id=order.item.id)
    
    # Get the item name
    item_name = listing.name
    
    # Get the owner from listing.owner_id
    owner_id = listing.owner_id
    
    # Get the owner object
    owner_object = get_object_or_404(User, id=owner_id)
    
    # Get the owner name
    owner = owner_object.first_name
    
    # Get the renter
    renter_id = order.renter_id
    
    # Get the renter object
    renter_object = get_object_or_404(User, id=renter_id)
    
    # Get the renter name
    renter = renter_object.first_name
    
    # Get the start and end dates
    start_date = order.start_date
    end_date = order.end_date
    
    # Encrypt the email 
    key = Fernet.generate_key()
    fernet =  Fernet(key)
    email = owner_object.email
    enc_email = fernet.encrypt(email.encode())
    
    # Load the email template
    html_content = render_to_string('order_receipt_owner.html', {
        'owner': owner,
        'renter': renter,
        'item_name': item_name,
        'start_date': start_date,
        'end_date': end_date
    })
    
    # Load the text content
    text_content = render_to_string('order_receipt_owner.txt', {
        'owner': owner,
        'renter': renter,
        'item_name': item_name,
        'start_date': start_date,
        'end_date': end_date
    })
    
    # Create EmailMultiAlternatives object to include both versions
    subject = "New Order Notification"
    from_email = "noreply@dybedahlserver.net"
    to_email = fernet.decrypt(enc_email).decode()
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, "text/html")
    
    # Send the email
    msg.send()

def send_order_email_receipt(order):
    # Send an email receipt to the renter that the order has been placed
    # Get the listing from listing id
    listing = get_object_or_404(Item, id=order.item.id)
    
    # Get the item name
    item_name = listing.name
    
    # Get the owner from listing.owner_id
    owner_id = listing.owner_id
    
    # Get the owner object
    owner_object = get_object_or_404(User, id=owner_id)
    
    # Get the owner name
    owner = owner_object.first_name
    
    # Get the renter
    renter_id = order.renter_id
    
    # Get the renter object
    renter_object = get_object_or_404(User, id=renter_id)
    
    # Get the renter name
    renter = renter_object.first_name
    
    # Get the start and end dates
    start_date = order.start_date
    end_date = order.end_date
    
    # Encrypt the email 
    key = Fernet.generate_key()
    fernet =  Fernet(key)
    email = renter_object.email
    enc_email = fernet.encrypt(email.encode())
    
    # Load the email template
    html_content = render_to_string('order_receipt_renter.html', {
        'owner': owner,
        'renter': renter,
        'item_name': item_name,
        'start_date': start_date,
        'end_date': end_date
    })
    
    # Load the text content
    text_content = render_to_string('order_receipt_renter.txt', {
        'owner': owner,
        'renter': renter,
        'item_name': item_name,
        'start_date': start_date,
        'end_date': end_date
    })
    
    # Create EmailMultiAlternatives object to include both versions
    subject = "Order Receipt"
    from_email = "noreply@dybedahlserver.net"
    to_email = fernet.decrypt(enc_email).decode()
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, "text/html")
    
    # Send the email
    msg.send()