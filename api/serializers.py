from rest_framework import serializers
from .models import Board, Post, comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','author','contents','created_date','like_count')