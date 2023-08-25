
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, GroupTraits
from .serializers import PostSerializer,GroupTraitsSerializer
from rest_framework import status
from django.utils import timezone
# Create your views here.
@api_view(['POST'])
def create_post(request):
    if request.method == 'POST':
        data = request.data
        
        group_traits_data = data.pop('group_traits')
        images = request.FILES.getlist('images')
        
        post_serializer = PostSerializer(data=data)
        if post_serializer.is_valid():
            post_instance = post_serializer.save(isManager=True, createdAt=timezone.now())
            
            group_traits_data['post'] = post_instance.pk
            group_traits_serializer = GroupTraitsSerializer(data=group_traits_data)
            if group_traits_serializer.is_valid():
                group_traits_serializer.save()
            else:
                post_instance.delete()
                return Response(group_traits_serializer.errors, status=400)
            
            # 여러 개의 이미지 업로드 처리
            for image in images:
                post_instance.images.create(image=image)
            
            return Response({'message': 'Post and GroupTraits created successfully'}, status=201)
        
        return Response(post_serializer.errors, status=400)
    
@api_view(['POST'])
def join_post(request, post_id):
    if request.method == 'POST':
        user = request.user  # 현재 로그인한 사용자
        
        post = get_object_or_404(Post, id=post_id)
        
        if user == post.user:
            return Response({'message': 'You cannot join your own post'}, status=status.HTTP_400_BAD_REQUEST)
        
        if post.number <= 0:
            return Response({'message': 'This post is already full'}, status=status.HTTP_400_BAD_REQUEST)
        
        post.participants.add(user)
        post.number -= 1
        post.save()
        
        return Response({'message': 'Joined the post successfully'}, status=status.HTTP_200_OK)
@api_view(['GET'])
def get_all_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=200)
