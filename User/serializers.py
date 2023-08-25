from rest_framework import serializers
from .models import *


# class LoginSerializer(serializers.ModelSerializer):


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = "__all__"
