from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

app_name = 'users'

#user models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to = "images/profile_picture", null=True, blank=True)
