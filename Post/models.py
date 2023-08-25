from django.db import models

from Server import Restaurant, User

# Create your models here.

class GroupTraits(models.Model):
    key=models.CharField(max_length=255, verbose_name='Key')
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
        return str(self.post)  # GroupTraits를 문자열로 표현할 때 Post의 key 값을 사용하도록 수정

class Post(models.Model):
    key=models.CharField(max_length=255, verbose_name='Key')
    createdAt=models.TimeField
    number=models.IntegerField
    comment=models.TextField
    link=models.URLField
    isManager= models.BooleanField
    restaurant= models.OneToOneField(Restaurant,on_delete=models.CASCADE,) #restaurant랑 매핑하면 menu도 자동으로 매핑되는데 합치고 나서 봐야할듯
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    group_traits = models.OneToOneField(GroupTraits, on_delete=models.CASCADE, related_name='post')
    
    class Meta:
        verbose_name_plural = 'Post'

    def __str__(self):
        return self.key
    

    
