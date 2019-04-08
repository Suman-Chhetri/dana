from django.db import models

# Create your models here.


class Intro(models.Model):
    content =  models.TextField()

    def __str__(self):
      return self.content

class Aim(models.Model):
    content = models.TextField()

    def __str__(self):
      return self.content

class Service(models.Model):
    content = models.TextField()

    def __str__(self):
      return self.content

class GalleryImage(models.Model):
    name = models.CharField(max_length=30)
    level = models.PositiveIntegerField(default=10)
    picture = models.ImageField(upload_to = "images/gallery")