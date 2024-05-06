from django.test import TestCase, Client
from django.urls import reverse
from airfinn.models import User, Item
import json
from airfinn.models import ItemImage
import base64
from django.core.files.uploadedfile import SimpleUploadedFile



# # Create your tests here.
# # class UserTestCase(TestCase):
#     def setUp(self):
#         # Create a test user with create_user method
#         # Credentials of test user:
#         self.credentials = {
#             'username': 'tester@testing.mail.com',
#             'email': 'tester@testing.mail.com',
#             'password': 'password',
#             'first_name': 'testy',
#             'last_name': 'testington',
#             'address': '1234 Test St.',
#             'phone': '12345678'
#         }
        
#         self.user = User.objects.create_user(**self.credentials)
        
#         # Create a test item
#         self.item = Item.objects.create(name="Test Item", description="This is a test item", availability=True, condition="New", price_per_day=5.00, owner=self.user, location="Test Location")
    
#     def test_login(self):
#         # Test with correct credentials
#         login_data = {
#             'username': self.credentials['username'],
#             'password': self.credentials['password']
#         }
        
#         wrong_login_data = {
#             'username': self.credentials['username'],
#             'password': 'wrongpassword'
#         }
            
#         response = self.client.post(reverse('login'), data=json.dumps(login_data), content_type='application/json')

#         self.assertEqual(response.status_code, 200)

#         # Extract token from response
#         token = response.json().get('token')

#         # Include token in request headers for subsequent requests
#         headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}

#         # Make authenticated request
#         response = self.client.get(reverse('dashboard'), **headers)

#         # Test with incorrect credentials
#         response = self.client.post(reverse('login'), data=json.dumps(wrong_login_data), content_type='application/json')
        
#         self.assertEqual(response.status_code, 401)
                


class CreateItemTestCase(TestCase):
    def setUp(self):
        # Owner user
        self.user1 = {
            'username': 'tester@testing.mail.com',
            'email': 'tester@testing.mail.com',
            'password': 'password',
            'first_name': 'testy',
            'last_name': 'testington',
            'address': '1234 Test St.',
            'phone': '12345678'
        }

        # Create owner user
        self.owner = User.objects.create_user(**self.user1)
        
        # Set up test data
        self.item = Item.objects.create(
            name='Test Item',
            price_per_day=10.0,
            description='Test Description',
            availability=True,
            condition='Good',
            location='Test Location',
            postal_code='0910',
            category='Test Category',
            owner=self.owner
        )

        # Set up other test data and client
        self.url = reverse('create_item')
        self.client = Client()

    def test_create_item_authorized_users(self):
        # User1 login
        login_data = {
            'username': self.user1['username'],
            'password': self.user1['password']
        }

        # Log in the owner user
        response = self.client.post(reverse('login'), data=json.dumps(login_data), content_type='application/json')

        # Check if the user is logged in successfully
        self.assertEqual(response.status_code, 200)

        # Get token
        token = response.json().get('token') 
        
        # Simulated image data
        image_data = b'fake image data'

        # Encode image data to base64
        base64_data = base64.b64encode(image_data).decode()

        # Construct base64 URL
        base64_url = f"data:image/jpeg;base64,{base64_data}"

        # Create a simulated image file with base64 content
        image_file = SimpleUploadedFile("fake_image.jpg", base64.b64decode(base64_data), content_type="image/jpeg")

        # Create item data with the simulated image file
        item_data = {
            'name': 'Test Item',
            'price_per_day': 10.0,
            'description': 'Test Description',
            'availability': True,
            'condition': 'Used',
            'location': 'Test Location',
            'postal_code': '0910',
            'category': 'Test Category',
            'owner': self.owner.id,
            'images': image_file
        }
        print(f"item_data: {item_data}")


        # Make POST request to create item
        response = self.client.post(self.url, data=item_data)
        print(f"Response: {response}")

        # Check if item is created successfully
        self.assertEqual(response.status_code, 200)


# class EditListingTestCase(TestCase):
#     def setUp(self):
#         # Owner user
#         self.user1 = {
#             'username': 'tester@testing.mail.com',
#             'email': 'tester@testing.mail.com',
#             'password': 'password',
#             'first_name': 'testy',
#             'last_name': 'testington',
#             'address': '1234 Test St.',
#             'phone': '12345678'
#         }

#         # other user
#         self.user2 = {
#             'username': 'other@testing.mail.com',
#             'email': 'other@testing.mail.com',
#             'password': 'password123',
#             'first_name': 'other',
#             'last_name': 'nottestington',
#             'address': '5678 Test St.',
#             'phone': '22222222'
#         }

#         # Users
#         self.owner = User.objects.create_user(**self.user1)
#         self.noOwner = User.objects.create_user(**self.user2)
        
#         # Set up test data
#         self.item = Item.objects.create(name='Test Item', description='Test Description', price_per_day=10, location='Test Location', category='Test Category', owner=self.owner)

#         self.url = reverse('edit_listing', args=[self.item.id])
#         self.client = Client()

#     def test_owner_user(self):
#         # User1 login
#         login_data = {
#             'username': self.user1['username'],
#             'password': self.user1['password']
#         }

#         # Log in the owner user
#         response = self.client.post(reverse('login'), data=json.dumps(login_data), content_type='application/json')

#         # Check if the user is logged in successfully
#         self.assertEqual(response.status_code, 200)

#         # Get token
#         token = response.json().get('token') 

#         # update request data
#         updated_data = {
#         'name': 'Updated Item',
#         'description': 'This is an updated item',
#         'price_per_day': 10.00,
#         'location': 'Updated Location',
#         'category': 'Updated Category',
#         }

#         # Send PUT request
#         response = self.client.put(self.url, data=json.dumps(updated_data), content_type='application/json')
      
#         # Check if the item is updated successfully
#         self.assertEqual(response.status_code, 200)

#         self.assertEqual(Item.objects.get(id=self.item.id).name, updated_data['name'])
#         self.assertEqual(Item.objects.get(id=self.item.id).description, updated_data['description'])
#         self.assertEqual(Item.objects.get(id=self.item.id).price_per_day, updated_data['price_per_day'])
#         self.assertEqual(Item.objects.get(id=self.item.id).location, updated_data['location'])
#         self.assertEqual(Item.objects.get(id=self.item.id).category, updated_data['category'])

#     def test_no_owner(self):
#         login_data = {
#             'username': self.user2['username'],
#             'password': self.user2['password']
#         }

#         # Log in the owner user
#         response = self.client.post(reverse('login'), data=json.dumps(login_data), content_type='application/json')

#         # Check if the user is logged in successfully
#         self.assertEqual(response.status_code, 200)

#         # Get token
#         token = response.json().get('token') 

#         # try and update request data
#         updated_data = {
#         'name': 'Updated Item',
#         'description': 'This is an updated item',
#         'price_per_day': 11.00,
#         'location': 'Updated Location',
#         'category': 'Updated Category',
#         }

#         # Send PUT request
#         response = self.client.put(self.url, data=json.dumps(updated_data), content_type='application/json')

#         # Check if the item is not updated successfully
#         self.assertEqual(response.status_code, 403)

#         # The item should not be updated
#         self.assertNotEqual(Item.objects.get(id=self.item.id).name, updated_data['name'])
#         self.assertNotEqual(Item.objects.get(id=self.item.id).description, updated_data['description'])
#         self.assertNotEqual(Item.objects.get(id=self.item.id).price_per_day, updated_data['price_per_day'])
#         self.assertNotEqual(Item.objects.get(id=self.item.id).location, updated_data['location'])
#         self.assertNotEqual(Item.objects.get(id=self.item.id).category, updated_data['category'])
    
#     def test_invalid_data(self):
#         login_data = {
#             'username': self.user1['username'],
#             'password': self.user1['password']
#         }

#         # Log in the owner user
#         response = self.client.post(reverse('login'), data=json.dumps(login_data), content_type='application/json')

#         # Check if the user is logged in successfully
#         self.assertEqual(response.status_code, 200)

#         # Get token
#         token = response.json().get('token') 

#         # update request data
#         updated_data = {
#         'name': 'Updated Item',
#         'description': 'This is an updated item',
#         'price_per_day': 'invalid',
#         'location': 'Updated Location',
#         'category': 'Updated Category',
#         }

#         # Send PUT request
#         response = self.client.put(self.url, data=json.dumps(updated_data), content_type='application/json')
      
#         # Check if the item is updated successfully
#         self.assertEqual(response.status_code, 400)

#         # The item should not be updated
#         self.assertNotEqual(Item.objects.get(id=self.item.id).name, updated_data['name'])
#         self.assertNotEqual(Item.objects.get(id=self.item.id).description, updated_data['description'])
#         self.assertNotEqual(Item.objects.get(id=self.item.id).price_per_day, updated_data['price_per_day'])
#         self.assertNotEqual(Item.objects.get(id=self.item.id).location, updated_data['location'])
#         self.assertNotEqual(Item.objects.get(id=self.item.id).category, updated_data['category'])
    
#     def test_negative_price_input(self):
#         login_data = {
#             'username': self.user1['username'],
#             'password': self.user1['password']
#         }

#         # Log in the owner user
#         response = self.client.post(reverse('login'), data=json.dumps(login_data), content_type='application/json')

#         # Check if the user is logged in successfully
#         self.assertEqual(response.status_code, 200)

#         # Get token
#         token = response.json().get('token') 

#         # update request data
#         updated_data = {
#         'name': 'Updated Item',
#         'description': 'This is an updated item',
#         'price_per_day': -10.00,
#         'location': 'Updated Location',
#         'category': 'Updated Category',
#         }

#         # Send PUT request
#         response = self.client.put(self.url, data=json.dumps(updated_data), content_type='application/json')
      
#         # Check if the item is updated successfully
#         self.assertEqual(response.status_code, 400)

#         # The item should not be updated
#         self.assertNotEqual(Item.objects.get(id=self.item.id).name, updated_data['name'])
#         self.assertNotEqual(Item.objects.get(id=self.item.id).description, updated_data['description'])
#         self.assertNotEqual(Item.objects.get(id=self.item.id).price_per_day, updated_data['price_per_day'])
#         self.assertNotEqual(Item.objects.get(id=self.item.id).location, updated_data['location'])
#         self.assertNotEqual(Item.objects.get(id=self.item.id).category, updated_data['category'])
    
#     def test_partial_updates(self):
#         login_data = {
#             'username': self.user1['username'],
#             'password': self.user1['password']
#         }

#         # Log in the owner user
#         response = self.client.post(reverse('login'), data=json.dumps(login_data), content_type='application/json')

#         # Check if the user is logged in successfully
#         self.assertEqual(response.status_code, 200)

#         # Get token
#         token = response.json().get('token') 

#         # update request data
#         updated_data = {
#         'name': 'Updated Item',
#         'description': 'This is an updated item',
#         }

#         # Send PUT request
#         response = self.client.put(self.url, data=json.dumps(updated_data), content_type='application/json')
      
#         # Check if the item is updated successfully
#         self.assertEqual(response.status_code, 200)

#         self.assertEqual(Item.objects.get(id=self.item.id).name, updated_data['name'])
#         self.assertEqual(Item.objects.get(id=self.item.id).description, updated_data['description'])
#         self.assertEqual(Item.objects.get(id=self.item.id).price_per_day, 10)
#         self.assertEqual(Item.objects.get(id=self.item.id).location, 'Test Location')
#         self.assertEqual(Item.objects.get(id=self.item.id).category, 'Test Category')



   