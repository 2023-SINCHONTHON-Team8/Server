from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import Response, views
from rest_framework import status
from .models import Likes
from .serializers import LikesSerializer


""" class LoginView(views.APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({'message': "로그인 성공", 'data': serializer.validated_data}, status=HTTP_200_OK)
        return Response({'message': "로그인 실패", 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST) """


class LikesAPIView(views.APIView):
    serializer_class = LikesSerializer

    def get(self, request):
        likes = Likes.objects.all()
        serializer = LikesSerializer(likes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
