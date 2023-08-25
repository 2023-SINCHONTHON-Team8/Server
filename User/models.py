from django.db import models
from django.contrib.auth.models import AbstractUser

class Member(AbstractUser):
    GENDER_CHOICES = (("male", "남성"), ("female", "여성"))
    email = models.EmailField(max_length=128, unique=True, verbose_name="사용자이메일")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="성별")

    # Assuming these fields exist
    mannerTemp = models.IntegerField(default=0)  # assuming this is a number between 0 and 100
    spicy = models.IntegerField(default=1)  # assuming this is a number between 1 and 5

class Like(models.Model):
   member=models.OneToOneField(Member,on_delete=models.CASCADE)
   insta_vibes=models.BooleanField()
   local_legend=models.BooleanField()
   trending_spot=models.BooleanField()
   secret_spot=models.BooleanField()
   mara=models.BooleanField()
   hawaiian_pizza=models.BooleanField()
   cucumber=models.BooleanField()
   perilla_leaves=models.BooleanField()
   mint_choco=models.BooleanField()

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
