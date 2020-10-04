from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_map, name='map'),
    path('list_map', views.list_map, name='list_map'),
    path('show_map/<int:site_id>', views.show_map, name='show_map'),
    path('<int:site_id>/delete', views.delete_map, name='delete_map'),
]
