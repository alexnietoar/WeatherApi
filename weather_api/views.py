from decouple import config
from datetime import datetime
from rest_framework import views
from rest_framework import status
from .serializers import WeatherSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.cache import cache_page

import os
import requests

# Create your views here.

def convertCelsius(Kelvin):
    return int(Kelvin - 273.15)

@cache_page(2*60)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getWeather(request):
    city = request.GET.get('city', '')
    country = request.GET.get('country', '').lower()
    api_data = config('API_DATA').format(city,country)
    response = requests.get(api_data)
    content = response.json()

    city_weather = [{
        "location_name": "{0}, {1}".format(content['name'],content["sys"]["country"]),
        "temperature": "{0} C°".format(int(convertCelsius(content["main"]["temp"]))),
        "wind_speed": "{0} m/s".format(content["wind"]["speed"]),
        "cloudiness": "{0} %".format(content["clouds"]["all"]),
        "presure": "{0} hpa".format(content["main"]["pressure"]),
        "humidity": "{0} %".format(content["main"]["humidity"]),
        "sunrise": "{0}".format(datetime.utcfromtimestamp(int(content["sys"]["sunrise"])).strftime('%H:%M')),
        "sunset": "{0}".format(datetime.utcfromtimestamp(int(content["sys"]["sunset"])).strftime('%H:%M')),
        "geo_coordinates": "[{0},{1}]".format(content["coord"]["lat"],content["coord"]["lon"]),
        "requested_time": "{0}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        "forecast": {
            "temp_max":"{0} C°".format(int(convertCelsius(content["main"]["temp_max"]))),
            "temp_min":"{0} C°".format(int(convertCelsius(content["main"]["temp_min"]))),
        },
    }]

    results = WeatherSerializer(city_weather, many=True).data

    return Response(results,template_name=None)