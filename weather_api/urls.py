from django.conf.urls import url, include
from weather_api import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    url('', include('djoser.urls')),
    url('', include('djoser.urls.authtoken')),
    url('', views.getWeather, name="api-overview"),
    url('weather?city=Medellin&country=CO', cache_page(120)(views.getWeather), name= "weather-city"),
    url('weather?city=Medellin&country=CO', views.getWeather, name= "weather-city")
]