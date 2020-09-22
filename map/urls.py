from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path(r'', views.default_map, name='map'),
    path('list_map', views.list_map, name='list_map'),
    path('<int:site_id>', views.update_map, name='update_map'),
    path('list_cars/<int:site_id>/delete', views.delete_map, name='delete_map'),

]
