# Generated by Django 4.2 on 2024-04-09 21:16

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_cupon_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='image',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
        ),
    ]
