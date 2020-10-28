from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *

class WeatherSerializer(serializers.Serializer):
    location_name = serializers.CharField(max_length=200)
    temperature = serializers.CharField(max_length=200)
    wind_speed = serializers.CharField(max_length=200)
    cloudiness = serializers.CharField(max_length=200)
    presure = serializers.CharField(max_length=200)
    humidity = serializers.CharField(max_length=200)
    sunrise = serializers.CharField(max_length=200)
    sunset = serializers.CharField(max_length=200)
    geo_coordinates = serializers.CharField(max_length=200)
    requested_time = serializers.CharField(max_length=200)
    forecast = serializers.DictField()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name', 'phone')