from rest_framework import serializers
from .models import Post, Author


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['userId']

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
