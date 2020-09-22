from django.shortcuts import render, redirect
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

    map_form = MapForm()
    if request.method == 'POST':
        map_form = MapForm(request.POST)
    if map_form.is_valid():
        map_form.save()
        messages.success(request, 'Location successfully added')
    return redirect('/functions/list_cars')


"""Update Location"""


def show_map(request, site_id):
    try:
        site = Map.objects.get(pk=site_id)
    except Map.DoesNotExist:
        messages.error(request, 'There is no location with this id!')
        return redirect('map')
    map_form = MapForm(initial={
        'plz': site.plz,
        'location': site.location,
        'address': site.address,
        'country': site.country,
    })
    if request.method == 'POST':
        map_form = MapForm(request.POST, instance=site)
    if map_form.is_valid():
        site.plz = map_form.cleaned_data['plz']
        site.location = map_form.cleaned_data['location']
        site.address = map_form.cleaned_data['address']
        site.country = map_form.cleaned_data['country']
        site.save()
    messages.success(request, 'Location successfully updated.')
    return render('functions/map.html', {'map_form': map_form, 'site': site})


def delete_map(request, site_id):
    try:
        site = Map.objects.get(pk=site_id)
        site.delete()
        messages.success(request, 'Location successfully deleted.')
    except Map.DoesNotExist:
        messages.error(request, 'There is no location with this id.')
    return redirect('map')
