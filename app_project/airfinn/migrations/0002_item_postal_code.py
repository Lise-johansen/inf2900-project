# Generated by Django 5.0.1 on 2024-04-22 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airfinn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='postal_code',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
