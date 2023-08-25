from django.db import models
from django_enum_choices import EnumChoices

class Taste(EnumChoices):
    KOREAN = 'Korean'
    CHINESE = 'Chinese'
    JAPANESE = 'Japanese'
    WESTERN = 'Western'
    World = 'World'
    Buffet = 'Buffet'
    Cafe = 'Cafe'
    Pub = 'Pub'

class Restaurant(models.Model):
    restaurant_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    taste = models.CharField(
        max_length=10,
        choices=Taste.choices(),
        default=Taste.KOREAN
    )

    def __str__(self):
        return self.name

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    menu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=200)
    imageurl = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.menu_name
