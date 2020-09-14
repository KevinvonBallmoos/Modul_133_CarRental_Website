from django.shortcuts import render
from .models import Map
from .forms import MapForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


"""Map shows"""


def default_map(request):
    mapbox_access_token = 'pk.eyJ1Ijoic3Vic2NhcGVyIiwiYSI6ImNrZXdpbmpvODQzb2MycnBpb2VjZWVkNGcifQ.UsJOjWVXbrP7wmlIzWb2wQ'
    return render(request, 'functions/map.html', {'mapbox_access_token': mapbox_access_token})


"""Add a new Location"""


def list_map(request):
    location = Map.objects.all()
    form = MapForm()
    if request.method == 'POST':
        form = MapForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Location successfully added')
    return render(request, 'functions/list_cars.html', {'location': location, 'form': form})
