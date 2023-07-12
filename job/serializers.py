from rest_framework import serializers
from .models import Job, Like
from main.serializers import TypeSerializer, CompanySerializer, CategorySerializer, CitySerializer
from account.serializers import AccountSerializer, MyAccountSerializer


class JobListSerializer(serializers.ModelSerializer):
    types = TypeSerializer(read_only=True, many=True)
    company = CompanySerializer(read_only=True)
    author = AccountSerializer(read_only=True)
    location = CitySerializer(read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'author', 'title', 'types', 'location', 'company', 'price', 'working_day']


class JobUpdateSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    types = TypeSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'author', 'title', 'types', 'location', 'company', 'price', 'category', 'working_day', ]


class LikeGetSerializer(serializers.ModelSerializer):
    author = MyAccountSerializer(read_only=True)
    job = JobListSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'author', 'job']




