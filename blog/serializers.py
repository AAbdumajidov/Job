from rest_framework import serializers
from .models import Blog, SubContent, Comment
from main.serializers import CategorySerializer, TagSerializer


class SubContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubContent
        fields = ['id', 'blog', 'cover', 'sub_content']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'blog', 'body', 'parent_comment', 'top_level_comment_id', 'created_date']


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'body', 'image', 'comments']


class BlogDetailSerializer(serializers.ModelSerializer):
    subcontent = SubContentSerializer(read_only=True, many=True)
    tag = TagSerializer(read_only=True, many=True)
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'body', 'image', 'subcontent', 'tag', 'comments', 'created_date']
