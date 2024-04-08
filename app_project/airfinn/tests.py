from django.test import TestCase
from django.urls import reverse
from airfinn.models import User, Item
import json

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        # Create a test user with create_user method
        # Credentials of test user:
        self.credentials = {
            'username': 'tester@testing.mail.com',
            'email': 'tester@testing.mail.com',
            'password': 'password',
            'first_name': 'testy',
            'last_name': 'testington',
            'address': '1234 Test St.',
            'phone': '12345678'
        }
        
        self.user = User.objects.create_user(**self.credentials)
        
        # Create a test item
        self.item = Item.objects.create(name="Test Item", description="This is a test item", availability=True, condition="New", price_per_day=5.00, images="images/default.jpg", owner=self.user, location="Test Location")
    
    def test_login(self):
        # Test with correct credentials
        login_data = {
            'username': self.credentials['username'],
            'password': self.credentials['password']
        }
        
        wrong_login_data = {
            'username': self.credentials['username'],
            'password': 'wrongpassword'
        }
            
        response = self.client.post(reverse('login'), data=json.dumps(login_data), content_type='application/json')

        self.assertEqual(response.status_code, 200)

        # Extract token from response
        token = response.json().get('token')

        # Include token in request headers for subsequent requests
        headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}

        # Make authenticated request
        response = self.client.get(reverse('dashboard'), **headers)

        # Test with incorrect credentials
        response = self.client.post(reverse('login'), data=json.dumps(wrong_login_data), content_type='application/json')
        
        self.assertEqual(response.status_code, 401)


class EditListingTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Create a test item
        self.item = Item.objects.create(name="Test Item", description="This is a test item", price_per_day=5.00, location="Test Location", category="Test Category",  owner=self.user)

    def test_edit_listing_authenticated_owner(self):
        # update request data
        updated_data = {
            'name': 'Updated Item',
            'description': 'This is an updated item',
            'price_per_day': 10.00,
            'location': 'Updated Location',
            'category': 'Updated Category'
        }

        # Make PUT request to edit the item
        response = self.client.put(reverse('edit_listing', args=[self.item.id]), data=json.dumps(updated_data), content_type='application/json')

        # Check if the item is updated successfully
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Item.objects.get(id=self.item.id).name, updated_data['name'])
        self.assertEqual(Item.objects.get(id=self.item.id).description, updated_data['description'])
        self.assertEqual(Item.objects.get(id=self.item.id).price_per_day, updated_data['price_per_day'])
        self.assertEqual(Item.objects.get(id=self.item.id).location, updated_data['location'])
        self.assertEqual(Item.objects.get(id=self.item.id).category, updated_data['category'])
        
    def test_edit_listing_authenticated_non_owner(self):
        # Create another user who is not the owner
        non_owner = User.objects.create_user(username='nonowner', password='password')

        # update request data
        updated_data = {
            'name': 'Updated Item',
            'description': 'This is an updated item',
            'price_per_day': 10.00,
            'location': 'Updated Location',
            'category': 'Updated Category'
        }

        # Authenticate as non-owner user
        self.client.login(username='nonowner', password='password')

        # Make PUT request to edit the item
        response = self.client.put(reverse('edit_listing', args=[self.item.id]), data=json.dumps(updated_data), content_type='application/json')

        # Check if the non-owner is not allowed to edit the item
        self.assertEqual(response.status_code, 403)

    def test_edit_listing_unauthenticated_user(self):
        # Make PUT request without authentication
        response = self.client.put(reverse('edit_listing', args=[self.item.id]), data={}, content_type='application/json')

        self.assertEqual(response.status_code, 401)





                
      
     