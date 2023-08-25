from django.urls import path
from . import views
#from .views import *

app_name = "User"

urlpatterns = [
    # 기존 URL 패턴들
    path('signup/', views.signup_view, name='signup'),  # '/signup/' URL 패턴 추가
 # path('likes/', LikesAPIView.as_view(), name='likes') 
    # ...
]