import os
import django
import random
import sys

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_project.settings')
django.setup()

from airfinn.models import Item, User  # Import your model

def populate_user():
    first_name = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack', 'Kate', 'Liam', 'Mia', 'Noah', 'Olivia', 'Peter', 'Quinn', 'Rose', 'Sam', 'Tina', 'Uma', 'Vince', 'Wendy', 'Xander', 'Yara', 'Zane']
    last_name = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins', 'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy', 'Bailey', 'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray', 'Ramirez', 'James', 'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Ross', 'Henderson', 'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Washington', 'Butler', 'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander', 'Russell', 'Griffin', 'Diaz', 'Hayes']
    address = ['Langneset', 'Mobekken', 'Gruben', 'Havnegata', 'Kongens gate', 'Storgata', 'Sjøgata', 'Strandgata', 'Kirkegata']

    # Create 10 random users
    for _ in range(10):
        email = f'{random.randint(1000, 9999)}@example.com'
        password = f'{random.randint(1000, 9999)}'
        
        user = {
            'first_name': random.choice(first_name),
            'last_name': random.choice(last_name),
            'email': email,
            'username': email,
            'address': random.choice(address),
            'phone': random.randint(11111111, 99999999),
            'password': password,
        }
        # Create a random user
        User.objects.create_user(**user)
        
def create_test_user():
    # create a test user for testing purposes. with inputs from terminal
    email = input('Enter email: ')
    password = input('Enter password: ')
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    address = input('Enter address: ')
    phone = input('Enter phone number: ')
    
    user = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'username': email,
        'address': address,
        'phone': phone,
        'password': password,
    }
    
    User.objects.create_user(**user)
    
    # create 10 listings for the test user using populate_listings()
    populate_listings(email)

def populate_listings(user_email=None):
    categories = ['Electronics', 'Clothing', 'Books', 'Furniture', 'Sports Equipment', 'Instruments', 'Tools', 'Town Square',]
    conditions = ['New', 'Used', 'Refurbished']
    postal_locations = [
        ('0010', 'Oslo'),
        ('0210', 'Hamar'),
        ('0505', 'Bergen'),
        ('2000', 'Lillestrøm'),
        ('4007', 'Stavanger'),
        ('5805', 'Bergen'),
        ('7030', 'Trondheim'),
        ('9008', 'Tromsø'),
        ('9991', 'Kirkenes')
    ]
    
    # If user_email is provided, get the user from the database
    if user_email:
        try:
            user = User.objects.get(email=user_email)
        except User.DoesNotExist:
            print(f"User with email '{user_email}' does not exist.")
            return
    
        # Create ten random listings for the user
        for _ in range(10): 
            postal_code, location = random.choice(postal_locations) 
            data = {
                'name': f'Listing {_ + 1} for test user',
                'description': f'Description of item {_ + 1}',
                'availability': random.choice([True, False]),
                'condition': random.choice(conditions),
                'price_per_day': round(random.uniform(5.0, 50.0), 2),
                'location': location,
                'postal_code': postal_code,
                'category': random.choice(categories),
                'owner': user,
            }
            Item.objects.create(**data)
    else:
        # Get a random user from the database
        users = User.objects.all()
        if not users.exists():
            print("No users found in the database.")
            return
        
        # Create five random listings
        for _ in range(100):  
            postal_code, location = random.choice(postal_locations)
            data = {
                'name': f'Item {_ + 1}',
                'description': f'Description of item {_ + 1}',
                'availability': random.choice([True, False]),
                'condition': random.choice(conditions),
                'price_per_day': round(random.uniform(5.0, 50.0), 2),
                'location': location,
                'postal_code': postal_code,
                'category': random.choice(categories),
                'category': random.choice(categories),
                'owner': random.choice(users),

            }
            Item.objects.create(**data)


def main():
    args = sys.argv[1:]

    if args:
        if args[0] == '-listings':
            populate_listings()
            print('Listings populated')
        elif args[0] == '-test':
            create_test_user()
            print('Test user created')
        elif args[0] == '-user':
            populate_user()
            print('User populated')
        elif args[0] == '-all':
            populate_user()
            populate_listings()
            print('All populated')
    else:
        print('No arguments given. Use -listings to populate listings, -user to populate user, or -all to populate both.')

if __name__ == '__main__':
    main()