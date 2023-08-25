from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken


# class LoginSerializer(serializers.ModelSerializer):

class LoginSerializer(serializers.ModelSerializer):
    username = models.CharField(max_length=32, verbose_name="사용자명")
    password = models.CharField(max_length=64, verbose_name="비밀번호")

    class Meta:
        model = Member
        fields = ['username', 'password']

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)

        if Member.objects.filter(username=username).exists():
            member = Member.objects.get(username=username)
            if not member.check_password(password):
                raise serializers.ValidationError('잘못된 비밀번호입니다.')
            else:
                token = RefreshToken.for_user(Member)
                refresh = str(token)
                access = str(token.access_token)

                data = {
                    'id': member.id,
                    'access_token': access
                }

                return data
        else:
            raise serializers.ValidationError('존재하지 않는 사용자입니다.')


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = "__all__"