from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Member(AbstractUser):
    GENDER_CHOICES = (("male", "남성"), ("female", "여성"))
    email = models.EmailField(max_length=128, unique=True, verbose_name="사용자이메일")
    # username = models.CharField(max_length=32, verbose_name="사용자명")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="성별")

    """ manner_temp = 
    post_list = 
    spicy = 1~5 """
