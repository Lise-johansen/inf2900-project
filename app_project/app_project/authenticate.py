from django.contrib.auth.models import User
from django.utils.functional import SimpleLazyObject
from django.middleware.csrf import get_token
from django.http import JsonResponse

class TokenAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the token from the request cookie
        token = request.COOKIES.get('user_id')

        # Authenticate the user using the token
        user = SimpleLazyObject(lambda: self.authenticate(token))

        # Set the authenticated user on the request
        request.user = user

        response = self.get_response(request)

        return response

    def authenticate(self, token):
        # Implement your token authentication logic here
        # For example, retrieve the user based on the token
        # This is just a placeholder implementation
        if token:
            try:
                # Get the user associated with the token
                user = User.objects.get(auth_token=token)
                return user
            except User.DoesNotExist:
                pass

        # If authentication fails, return AnonymousUser
        return User.objects.get(id=1)  # Replace with your AnonymousUser
