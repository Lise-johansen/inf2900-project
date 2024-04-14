import os
import django
import random
import sys

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_project.settings')
django.setup()

from airfinn.models import Item, User  # Import your model

def populate_user():
    # Create a random email since emails must be unique
    email = f'{random.randint(1000, 9999)}@example.com'
    password = f'{random.randint(1000, 9999)}'

    user = {
        'first_name': f'Pop',
        'last_name': f'User',
        'email': email,
        'username': email,
        'address': f'Pop User Street',
        'phone': f'12345678',
        'password': password,
    }

    #Create a single basic user
    User.objects.create_user(**user)

def populate_listings():
    categories = ['Electronics', 'Clothing', 'Books', 'Furniture', 'Sports Equipment', 'Instruments', 'Tools', 'Town Square',]
    conditions = ['New', 'Used', 'Refurbished']
    locations = ['Langneset', 'Mobekken', 'Gruben']
    user = User.objects.get(id=1)

    user = User.objects.get(id=1)

    for _ in range(5):  # Create five random listings
        data = {
            'name': f'Item {_ + 1}',
            'description': f'Description of item {_ + 1}',
            'availability': random.choice([True, False]),
            'condition': random.choice(conditions),
            'price_per_day': round(random.uniform(5.0, 50.0), 2),
            'location': random.choice(locations),
            'category': random.choice(categories),
            'category': random.choice(categories),
            'owner': user

        }
        Item.objects.create(**data)

def main():
    args = sys.argv[1:]

    if args:
        if args[0] == '-listings':
            populate_listings()
            print('Listings populated')
        elif args[0] == '-user':
            populate_user()
            print('User populated')
        elif args[0] == '-all':
            populate_listings()
            populate_user()
            print('All populated')
    else:
        print('No arguments given. Use -listings to populate listings, -user to populate user, or -all to populate both.')

if __name__ == '__main__':
    main()
