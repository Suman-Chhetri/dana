from django.db import models

# Create your models here.

app_name = 'users'

class Member(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name =  models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    rank = models.PositiveIntegerField(default=10)
    role = models.CharField(max_length=30, default='Staff')
    status = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to = "images/profile_picture", null=True, blank=True)

    def __str__(self):
        return self.email