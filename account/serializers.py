from rest_framework import serializers
from .models import Account, WorkHistory
from main.serializers import CitySerializer


class AccountSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'username', 'first_name', 'last_name', 'image', 'bio', 'role', 'city']


class MyAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'email', 'role', 'first_name', 'last_name', 'image_url', 'bio', 'created_date')


class WorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHistory
        fields = ['id', 'account', 'company', 'location', 'start_date', 'end_date', 'is_current']

