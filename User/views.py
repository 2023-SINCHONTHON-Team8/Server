import random
from django.forms import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.core.validators import validate_email
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import *
import json
from User.models import Member

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
'''
# Create your views here.
class RegistrationAPIView(APIView):
    #클라이언트로부터 받은 데이터 처리
    email = requests.data.get('email')
    username = requests.data.get('username')
    password = requests.data.get('password')
    gender = requests.data.get('gender') #남성/여성 선택

    # Univcert API 호출 및 회원가입 처리
        # univcert_api_url = ""  
        univcert_data = {
            "email": email,
            "username": username,
            "password": password,
            "gender": gender,
        }
        
        response = requests.post(univcert_api_url, json=univcert_data)

        if response.status_code == 200:
            # 회원가입 성공 시, 여기서 추가적인 처리 (인증 메일 발송 등)
            return Response({"message": "회원가입이 성공적으로 완료되었습니다."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "회원가입에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST)

'''
#학교이메일 주소만 허용
def validate_email_domain(value):
    valid_domains = ['sogang.ac.kr','g.hongik.ac.kr', 'yonsei.ac.kr','ewhain.net']
    email = value.split('@')
    if len(email) == 2 and email[1] in valid_domains:
        return True
    raise ValidationError("서강,연대,이대,홍대대학교 도메인 주소를 통한 이메일 인증만 가능합니다.")


def generate_verification_code():
    return str(random.randint(100000, 999999))

def signup_view(request):
    print(request)
    if request.method == 'POST':
        print(request)
        data = json.loads(request.body)
        email = data.get('email')
        print(email)
        password = data.get('password')
        username = data.get('username')
        #school = data.get('school')

        try:
            #validate_email(email)  # 이메일 형식 검증
            validate_email_domain(email)  # 도메인 검증
        except ValidationError as e:
            return JsonResponse({'message': str(e)}, status=400)
        
        # 이미 존재하는 이메일인지 확인
        if Member.objects.filter(email=email).exists():
            return JsonResponse({'message': 'Email already exists'}, status=400)


        # 사용자 생성
        user = Member.objects.create_user(email=email, password=password,username=username)
        
        
        # jwt 토큰 접근
        token = TokenObtainPairSerializer.get_token(user)
        refresh_token = str(token)
        access_token = str(token.access_token)
        res = {
                "user": {
                    "email": user.email,
                    "nickname": user.username,
                },
                "message": "register successs",
                "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
            },

        
        response = JsonResponse(res, safe=False,status=201)

        return response
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
    

class LoginView(views.APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({'message': "로그인 성공", 'data': serializer.validated_data}, status=status.HTTP_200_OK)
        return Response({'message': "로그인 실패", 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LikesAPIView(views.APIView):
    serializer_class = LikesSerializer

    def get(self, request):
        likes = Likes.objects.all()
        serializer = LikesSerializer(likes, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        print(data)
        member = request.user
        
        # LikesSerializer에 member 정보 추가하여 직렬화
        serializer = LikesSerializer(data={**data, 'member': member.id})
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

