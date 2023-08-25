from django.db import models
from enum import Enum
from django_enum_choices.fields import EnumChoiceField

class Taste(Enum):
    KOREAN = 'Korean'
    CHINESE = 'Chinese'
    JAPANESE = 'Japanese'
    WESTERN = 'Western'
    WORLD = 'World'
    BUFFET = 'Buffet'
    CAFE = 'Cafe'
    PUB = 'Pub'

class Restaurant(models.Model):
    restaurant_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    taste = EnumChoiceField(Taste, default=Taste.KOREAN)

def __str__(self):
        return self.name

class Menu(models.Model):
   menu_id=models.AutoField(primary_key=True)
   name=models.CharField(max_length=255)
   price=models.CharField(max_length=200)
   imageurl=models.ImageField(upload_to='images/')
   restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE)

def __str__(self):
        return self.name
