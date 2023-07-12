from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer, BlogDetailSerializer


class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetailAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer

