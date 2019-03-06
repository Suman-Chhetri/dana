from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

# Create your models here.

app_name = 'users'

#user models
class UserManager(BaseUserManager):
    def create_user(self, email, username, password, alias=None):
        if not email:
            raise ValueError("Please enter email address.")
        if not username:
            raise ValueError("Please enter valid username.")
        if not password:
            raise ValueError("Please enter strong password")
        if not alias:
            alias = username
        
        user = self.model(
             email = self.normalize_email(email),
             username = username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password):
        self.create_user(email, username, password)
        
        user.is_staff()
        user.is_superuser = True
        user.save()
        return user

class CustomUser(AbstractUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    rank = models.PositiveIntegerField(default=10)
    role = models.CharField(max_length=30, default='')
    status = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to = "images/profile_picture", null=True, blank=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.email