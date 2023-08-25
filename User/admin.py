from django.contrib import admin
from Post.models import Post
from Restaurant.models import Restaurant
from Post.models import GroupTraits
from User.models import *

# Register your models here.
admin.site.register(Member)
admin.site.register(Restaurant)
admin.site.register(Post)
admin.site.register(GroupTraits)
admin.site.register(Likes)

