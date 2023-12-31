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

    
    class Meta:
        verbose_name_plural = 'GroupTraits'

    def __str__(self):
        return str(self.id)  # GroupTraits를 문자열로 표현할 때 Post의 key 값을 사용하도록 수정

class Post(models.Model):
    key = models.AutoField(primary_key=True) 
    post_name=models.CharField(max_length=255,default=None)
    createdAt=models.TimeField
    number=models.IntegerField
    comment=models.TextField
    link=models.URLField
    isManager= models.BooleanField
    restaurant= models.OneToOneField(Restaurant,on_delete=models.CASCADE,) #restaurant랑 매핑하면 menu도 자동으로 매핑되는데 합치고 나서 봐야할듯
    user=models.ForeignKey(Member, on_delete=models.CASCADE)
    group_traits = models.ForeignKey(GroupTraits, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='post_images/', blank=True, null=True, verbose_name='Images')
    
    # ManyToMany 필드로서 참여한 사용자들을 나타냅니다.
    participants = models.ManyToManyField(Member, related_name='joined_posts', blank=True)
    class Meta:
        verbose_name_plural = 'Post'

    def __str__(self):
        return self.post_name
    

    
class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='post_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/')

    def __str__(self):
        return f"Image for Post {self.post.key}"
