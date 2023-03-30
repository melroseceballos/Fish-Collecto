from django.db import models
from django.urls import reverse

# MEAL CHOICES TUPLE
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

  # PLANTS model
class Plants(models.Model):
  name = models.CharField(max_length= 100)
  size = models.CharField(max_length= 100)
  

# Create your models here.
class Fish (models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color = models.TextField(max_length=250)
    age = models.IntegerField()
    # MANY TO MANY RELATIONSHIP
    plants = models.ManyToManyField(Plants)

# FEEDING model
class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
	 choices=MEALS,
	 default=MEALS[0][0]
  )

  # Create a cat_id FK
  fish = models.ForeignKey(Fish, on_delete=models.CASCADE)

#OVERRIDING STRING
  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
     ordering=['-date']

# REDIRECT FISH CREATE
def get_absolute_url(self):
    return reverse('detail', kwargs={'fish_id': self.id})

# REDIRECT PLANTS CREATE  
def get_absolute_ulr(self):
   return reverse('plants_details', kwargs={'plants_id': self.id})