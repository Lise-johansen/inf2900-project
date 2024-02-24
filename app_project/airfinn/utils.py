from django.contrib.auth.models import User
from .models import Item
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.core.serializers import serialize
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


def search_items(request):
    category = request.GET.get('category', '')
    query = request.GET.get('q', '')

    items = Item.objects.all()
    if category:
        items = items.filter(category=category)
    if query:
        items = items.filter(name__icontains=query)

    # Serialize the queryset of items
    data = serialize('json', items)
    return JsonResponse(data, safe=False)

def edit_listing(request, id):
    """
    Function to edit an existing listing.
    ID is the primary key of the item to be edited.
    """
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return HttpResponseNotFound('Item not found')

    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    # Validate and update item fields
    item.name = request.POST.get('name', item.name)
    item.description = request.POST.get('description', item.description)
    item.availability = request.POST.get('availability', item.availability)
    item.condition = request.POST.get('condition', item.condition)
    item.price_per_day = request.POST.get('price_per_day', item.price_per_day)
    item.images = request.FILES.get('images', item.images)
    item.owner = request.POST.get('owner', item.owner)
    item.location = request.POST.get('location', item.location)
    item.category = request.POST.get('category', item.category)

    try:
        item.save()
        return JsonResponse({'message': 'Item updated successfully'}, status=200)
    except Exception as e:
        return JsonResponse({'message': f'Error updating item: {str(e)}'}, status=500)
