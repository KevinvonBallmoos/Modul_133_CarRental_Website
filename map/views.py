from django.shortcuts import render
from .models import Map
from .forms import MapForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def show_map(request):

    mapbox_access_token = 'pk.eyJ1Ijoic3Vic2NhcGVyIiwiYSI6ImNrZXdteTZtYzRnODUyenBjempkdG9la2cifQ.iOzJ7YG9sgc_rhegxJOFTw'
    return render(request, 'functions/show_map.html',
                  {'mapbox_access_token': mapbox_access_token})


def list_map(request):
    location = Map.objects.all()
    form = MapForm()
    if request.method == 'POST':
        form = MapForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Location successfully added')
    return render(request, 'functions/show_map.html', {'location': location, 'form': form})
