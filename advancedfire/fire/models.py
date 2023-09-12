# fire/models.py

from django.db import models
from tinymce.models import HTMLField

class Staff(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    photo = models.ImageField()
    post = models.TextField()
    detail = HTMLField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'fire'  # Specify the app label for the Staff model
class Review(models.Model):
    name = models.CharField(max_length=250)
    review = models.TextField(max_length=5000)