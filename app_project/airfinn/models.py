from django.db import models

# Create your models here.


class User(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    availability = models.BooleanField(default=True)
    condition = models.CharField(max_length=100, default='')
    price_per_day = models.FloatField(max_length=1000, default=0.0)
    images = models.ImageField(
        upload_to='images/', default='images/default.jpg')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    location = models.CharField(max_length=100, default='')
    category = models.CharField(max_length=100, default='')
