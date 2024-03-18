import os
import django
import random

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_project.settings')
django.setup()

from airfinn.models import Item  # Import your model
from airfinn.models import User


def populate_listings():
    categories = ['Electronics', 'Clothing', 'Books', 'Furniture', 'Sports Equipment']
    conditions = ['New', 'Used', 'Refurbished']
    locations = ['Langneset', 'Mobekken', 'Gruben']
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
            'owner': user

        }
        Item.objects.create(**data)

if __name__ == '__main__':
    populate_listings()
