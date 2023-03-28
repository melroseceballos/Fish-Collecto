from django.db import models

# Create your models here.
class Fish (models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color = models.TextField(max_length=250)
    age = models.IntegerField()

def __str__(self):
    return f'{self.name} {(self.id)}'