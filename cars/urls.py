from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.list_cars, name='list_cars'),
    path('show_cars/<int:car_id>', views.show_cars, name='show_cars'),
    path('list_cars/<int:car_id>/delete', views.delete_cars, name='delete_cars'),

]
