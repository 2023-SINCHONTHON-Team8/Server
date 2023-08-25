from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Member(AbstractUser):
    GENDER_CHOICES = (("male", "남성"), ("female", "여성"))  # enum
    email = models.EmailField(max_length=128, unique=True, verbose_name="사용자이메일")
    # username = models.CharField(max_length=32, verbose_name="사용자명")
    # password = models.CharField(max_length=64, verbose_name="비밀번호")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="성별")
    """ manner_temp = 
    post_list = 
    spicy = 1~5 """


class Likes(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    insta_vibes = models.BooleanField(default=False)  # 인스타감성
    local_legend = models.BooleanField(default=False)  # 이지역터줏대감
    trending_spot = models.BooleanField(default=False)  # 신상핫플
    secret_spot = models.BooleanField(default=False)  # 나만아는곳
    # 추가적인 그룹 특성
    # Add the custom traits "민초" and "고수"
    mint_choco = models.BooleanField(default=False)
    perilla_leaves = models.BooleanField(default=False)
    mara = models.BooleanField(default=False)  # 마라
    hawaiian_pizza = models.BooleanField(default=False)  # 하와이안피자
    cucumber = models.BooleanField(default=False)  # 오이

    class Meta:
        verbose_name_plural = "Likes"

    def __str__(self):
        return str(self.member)
