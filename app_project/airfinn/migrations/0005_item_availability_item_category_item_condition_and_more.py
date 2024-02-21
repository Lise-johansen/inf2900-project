# Generated by Django 5.0.1 on 2024-02-20 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airfinn', '0004_item_description_item_images_item_price_per_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='availability',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='condition',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(default='test', on_delete=django.db.models.deletion.CASCADE, to='airfinn.user'),
        ),
    ]
