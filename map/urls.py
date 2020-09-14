from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path(r'', views.default_map, name='map'),
    path('', views.list_map, name='list_map'),
]
