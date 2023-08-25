from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, password, **extra_fields)

# Create your models here.
class Member(AbstractUser):
    GENDER_CHOICES = (("male", "남성"), ("female", "여성"))
    email = models.EmailField(max_length=128, unique=True, verbose_name="사용자이메일")
    username = models.CharField(max_length=32, verbose_name="사용자명")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="성별")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    spicy = models.IntegerField(default=1)
    
     # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 email으로 설정 (이메일로 로그인)
    USERNAME_FIELD = 'email'
    
    # REQUIRED_FIELDS 수정: 'email'을 제외한 필드들만 남김
    REQUIRED_FIELDS = ['username']

    """ manner_temp = 
    post_list = 
    spicy = 1~5 """

class Likes(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE, default=None)
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
        verbose_name_plural = 'Likes'
        
    def __str__(self):
        return str(self.member)
    
def similarity(self, other_user):
        mannerTemp_similarity = abs(self.mannerTemp - other_user.mannerTemp) / 100.0
        spicy_similarity = abs(self.spicy - other_user.spicy) / 10.0
        
        like_fields=['insta_vibes','local_legend','trending_spot','secret_spot',
                     'mara','hawaiian_pizza', 'cucumber', 'perilla_leaves', 'mint_choco']
        
        like_similarity=sum([int(getattr(self.like,f)==getattr(other_user.like,f)) for f in like_fields])/len(like_fields)
        
        return mannerTemp_similarity * 0.25 + spicy_similarity * 0.25 + like_similarity*0.5


def get_similar_users(user,top_n=5):
    users=Member.objects.exclude(id=user.id)
    similarities=[(other_user,user.similarity(other_user)) for other_user in users]
    similarities.sort(key=lambda x: x[1],reverse=True)

    return [user for user,similarity in similarities[:top_n]]


def recommend_posts(user):
    from Post.models import Post

    similar_users=get_similar_users(user)

    recommended_posts=[]

    for similar_user in similar_users:
        posts_by_similar_user = Post.objects.filter(author=similar_user)

    unseen_posts_by_similar_user=posts_by_similar_user.exclude(seen_by__id=user.id)

    recommended_posts.extend(unseen_posts_by_similar_user)

    return recommended_posts 
