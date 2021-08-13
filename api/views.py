# Create your views here.

# api/views.py

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer

# Create your views here.
@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!")

@api_view(['GET'])
def postAPI(request):
    allPost = Post.objects.all()
    serializer = PostSerializer(allPost, many = True)
    return Response(serializer.data)