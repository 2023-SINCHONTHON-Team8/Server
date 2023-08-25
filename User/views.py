""" from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

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






 """
