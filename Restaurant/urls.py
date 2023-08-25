from django.urls import path
from . import views

urlpatterns = [
    # 다른 URL 패턴들
    path('restaurants/', views.get_all_restaurants, name='get_all_restaurants'),
]
