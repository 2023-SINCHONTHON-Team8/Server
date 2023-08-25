from django.urls import path
from . import views

urlpatterns = [
    # 기존 URL 패턴들
    path('signup/', views.signup_view, name='signup'),  # '/signup/' URL 패턴 추가
    # ...
]