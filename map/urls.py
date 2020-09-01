from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url


urlpatterns = [
path('map', views.map, name='map'),
]