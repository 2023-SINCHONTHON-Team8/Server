from rest_framework import serializers
from .models import Post, GroupTraits

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class GroupTraitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupTraits
        fields = '__all__'
