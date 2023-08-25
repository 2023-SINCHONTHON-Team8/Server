from django.urls import path
from .views import *

urlpatterns = [
    path('create_post/', create_post, name='create_post'),
    path('join/<int:post_id>/', join_post, name='join_post'),
    path('posts/', get_all_posts, name='get_all_posts'),
    path('posts/<int:post_id>/', get_post_detail, name='get_post_detail'),  
]