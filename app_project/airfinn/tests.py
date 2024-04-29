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
        self.item = Item.objects.create(name="Test Item", description="This is a test item", availability=True, condition="New", price_per_day=5.00, owner=self.user, location="Test Location")
    
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



                
      
     