from django.shortcuts import render, redirect
from .models import Cars
from .forms import CarForm
from map.forms import MapForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

"""Add a new Car"""


def list_cars(request):
    cars = Cars.objects.all()
    car_form = CarForm()
    map_form = MapForm()
    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES)
    if car_form.is_valid():
        car_form.save()
        messages.success(request, 'Car successfully added')
        cars = Cars.objects.all()
    return render(request, 'functions/list_cars.html', {'cars': cars, 'car_form': car_form, 'map_form': map_form})


def list_map(request):
    form = MapForm()
    return render(request, 'functions/list_cars.html', {'form': form})


"""Update car"""


def show_cars(request, cars_id):
    try:
        car = Cars.objects.get(pk=cars_id)
    except Cars.DoesNotExist:
        messages.error(request, 'There is no car with this id!')
        return redirect(list_cars)
    form = CarForm(initial={
        'brand': car.brand,
        'model': car.model,
        'image': car.image,
        'ps': car.ps,
        'details': car.details,
        'location': car.location,
    })
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            car.brand = form.cleaned_data['first_name']
            car.model = form.cleaned_data['last_name']
            car.image = form.cleaned_data['image']
            car.ps = form.cleaned_data['ps']
            car.details = form.cleaned_data['details']
            car.location = form.cleaned_data['location']
            car.save()
        messages.success(request, 'Car successfully updated')
    return render(request, 'functions/show_cars.html', {'form': form, 'car': car})
