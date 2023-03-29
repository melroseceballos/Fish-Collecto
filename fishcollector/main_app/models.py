from django.db import models
from django.urls import reverse
# Create your models here.
class Fish (models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color = models.TextField(max_length=250)
    age = models.IntegerField()

def get_absolute_url(self):
    return reverse('detail', kwargs={'fish_id': self.id})