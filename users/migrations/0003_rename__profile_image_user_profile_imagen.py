# Generated by Django 4.0.5 on 2022-07-05 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_profile__profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profile',
            old_name='_profile_image',
            new_name='imagen',
        ),
    ]
