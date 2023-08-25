from django.shortcuts import render
from .models import Restaurant, Menu
from .serializers import RestaurantSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


def index(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants}
    return render(request, 'restaurant/index.html', context)

def detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    menus = restaurant.menu_set.all()
    context = {'restaurant': restaurant, 'menus': menus}
    return render(request, 'restaurant/detail.html', context)


@api_view(['GET'])
@permission_classes([AllowAny])  # 인증 없이 접근 가능하도록 설정
def get_all_restaurants(request):
    if request.method == 'GET':
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)  # 다수의 객체를 직렬화해야 하므로 `many=True`
        return Response(serializer.data)

