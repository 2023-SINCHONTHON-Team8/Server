from django.db import models

from Server import User

# Create your models here.
class Post(models.Model):
    key=models.CharField(max_length=255, verbose_name='Key')
    createdAt=models.TimeField
    number=models.IntegerField
    comment=models.TextField
    link=models.URLField
    isManager= models.BooleanField
    #restaurant= models.OneToOneField(Restaurant,on_delete=models.CASCADE,) #restaurant랑 매핑하면 menu도 자동으로 매핑되는데 합치고 나서 봐야할듯
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Post'

    def __str__(self):
        return self.key
    
class GroupTraits(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='group_traits')
    
    class Meta:
        verbose_name_plural = 'GroupTraits'

    def __str__(self):
        return self.key
    
