from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Cars, Map
from .forms import CarForm
from map.forms import MapForm
from django.contrib import messages


@login_required()
def list_cars(request):
    """
    add car
    param: user request
    return: list_cars.html
    """
    cars = Cars.objects.all()
    sites = Map.objects.all()
    car_form = CarForm()
    map_form = MapForm()
    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES)
    if car_form.is_valid():
        car_form.save()
        messages.success(request, 'Car successfully added')
    return render(request, 'functions/list_cars.html', {'cars': cars, 'car_form': car_form, 'sites': sites, 'map_form':
                                                        map_form})


@login_required()
def show_cars(request, car_id):
    """
    update car
    param: user request, car_id
    returns: show_cars.html
    """
    try:
        car = Cars.objects.get(pk=car_id)
    except Cars.DoesNotExist:
        messages.error(request, 'There is no car with this id!')
        return redirect(list_cars)
    car_form = CarForm(initial={
        'brand': car.brand,
        'model': car.model,
        'image': car.image,
        'ps': car.ps,
        'details': car.details,
        'location': car.location,
        'types': car.types,
    })
    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES, instance=car)
        if car_form.is_valid():
            car.brand = car_form.cleaned_data['brand']
            car.model = car_form.cleaned_data['model']
            car.image = car_form.cleaned_data['image']
            car.ps = car_form.cleaned_data['ps']
            car.details = car_form.cleaned_data['details']
            car.location = car_form.cleaned_data['location']
            car.types = car_form.cleaned_data['types']
            car.save()
        messages.success(request, 'Car successfully updated')
    return render(request, 'functions/show_cars.html', {'car_form': car_form, 'car': car})


@login_required()
def delete_cars(request, car_id):
    """
    delete car
    param: user request, car_id
    return: redirect list_cars
    """
    try:
        car = Cars.objects.get(pk=car_id)
        car.delete()
        messages.success(request, 'Successfully deleted')
    except Cars.DoesNotExist:
        messages.success(request, 'There is no car with this id!')
    return redirect('list_cars')
