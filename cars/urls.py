from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.list_cars, name='list_cars'),
    path('/show_cars/<int:cars_id>', views.show_cars, name='show_cars')

]
