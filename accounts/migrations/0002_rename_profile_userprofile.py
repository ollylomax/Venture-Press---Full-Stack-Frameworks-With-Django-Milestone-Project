# Generated by Django 3.2.13 on 2022-06-30 18:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_order_user_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='UserProfile',
        ),
    ]
