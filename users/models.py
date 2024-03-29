from distutils.command.upload import upload
from threading import _profile_hook
from django.db import models
from django.contrib.auth.models import User

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "user_profile")
    phone = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to = "profile_image")
