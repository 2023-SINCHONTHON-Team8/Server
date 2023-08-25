from django.shortcuts import render
from .models import Restaurant, Menu

def index(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants}
    return render(request, 'restaurant/index.html', context)

def detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    menus = restaurant.menu_set.all()
    context = {'restaurant': restaurant, 'menus': menus}
    return render(request, 'restaurant/detail.html', context)
