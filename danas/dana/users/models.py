from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

app_name = 'users'

#user models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=30, default='')
    status = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to = "images/profile_picture", null=True, blank=True)

