from django.contrib.auth.models import User
from .models import Item
from django.http import JsonResponse, HttpResponseNotAllowed
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
