
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_cars, name='list_cars'),
    path('show_cars/<int:car_id>', views.show_cars, name='show_cars'),
    path('list_cars/<int:car_id>/delete', views.delete_cars, name='delete_cars'),

]
