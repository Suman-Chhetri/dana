from django.db import models
from django.utils import timezone
from django.urls import reverse
from users.models import CustomUser


# Create your models here.

class News(models.Model):
    added_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='adminEmail')
    title = models.CharField(max_length=100)
    dateAdded = models.DateTimeField(default=timezone.now())
    picture = models.ImageField(upload_to = "images/news")
    content =  models.TextField()


    def __str__(self):
      return self.title
