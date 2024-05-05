from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    last_login = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_picture_url = models.URLField(default='https://rentopia-images.dybedahlserver.net/default_profile_picture.jpg')
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username
    
    
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    availability = models.BooleanField(default=True)
    condition = models.CharField(max_length=100, default='')
    price_per_day = models.FloatField(max_length=1000, default=0.0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    postal_code = models.CharField(max_length=4)
    location = models.CharField(max_length=100, default='')
    category = models.CharField(max_length=100, default='')
    rating = models.FloatField(default=0.0)
    
class ItemImage(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField(default='https://rentopia-images.dybedahlserver.net/default_item_picture.jpg')
    
    
# Model for creating a message platform for users to send messages to each other    
class Conversation(models.Model):
    id = models.AutoField(primary_key=True)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations_as_user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations_as_user2')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField(default='')
    image = models.URLField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    
class Favourites(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='favourites')