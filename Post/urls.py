from django.urls import path
from .views import *

urlpatterns = [
    path('api/create_post/', create_post, name='create_post'),
    path('join/<int:post_id>/', join_post, name='join_post'),  
]