from django.db import models

from Restaurant.models import *
from User.models import *


# Create your models here.


class GroupTraits(models.Model):
    # 그룹 특성을 나타내는 불린 필드들
    quiet_dining = models.BooleanField(default=False)  # 조용한 식사
    enfp_meeting = models.BooleanField(default=False)  # ENFP 모임
    food_fighter = models.BooleanField(default=False)  # 푸드파이터
    news_club = models.BooleanField(default=False)  # 소식클럽
    insta_vibes = models.BooleanField(default=False)  # 인스타감성
    local_legend = models.BooleanField(default=False)  # 이지역터줏대감
    trending_spot = models.BooleanField(default=False)  # 신상핫플
    secret_spot = models.BooleanField(default=False)  # 나만아는곳
    # 추가적인 그룹 특성
    mara = models.BooleanField(default=False)  # 마라
    hawaiian_pizza = models.BooleanField(default=False)  # 하와이안피자
    cucumber = models.BooleanField(default=False)  # 오이

    class Meta:
        verbose_name_plural = "GroupTraits"

    def __str__(self):
        return str(self.id)  # GroupTraits를 문자열로 표현할 때 Post의 key 값을 사용하도록 수정


class Post(models.Model):
    key = models.AutoField(primary_key=True)
    createdAt = models.TimeField
    number = models.IntegerField
    comment = models.TextField
    link = models.URLField
    isManager = models.BooleanField
    restaurant = models.OneToOneField(
        Restaurant,
        on_delete=models.CASCADE,
    )  # restaurant랑 매핑하면 menu도 자동으로 매핑되는데 합치고 나서 봐야할듯
    user = models.ForeignKey("User.Member", on_delete=models.CASCADE)
    group_traits = models.OneToOneField(
        GroupTraits, on_delete=models.CASCADE, related_name="post"
    )
    images = models.ImageField(
        upload_to="post_images/", blank=True, null=True, verbose_name="Images"
    )

    class Meta:
        verbose_name_plural = "Post"

    def __str__(self):
        return self.key
