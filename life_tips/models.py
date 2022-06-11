from django.db import models
from django.shortcuts import reverse, get_object_or_404
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]

    def get_absolute_url(self): 
        return reverse('life_tips')
