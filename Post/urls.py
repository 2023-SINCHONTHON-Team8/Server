from django.urls import path
from .views import *

urlpatterns = [
    path('api/create_post/', create_post, name='create_post'),
    path('join/<int:post_id>/', join_post, name='join_post'),
    path('api/posts/', get_all_posts, name='get_all_posts'),
    path('api/posts/<int:post_id>/', get_post_detail, name='get_post_detail'),  
]