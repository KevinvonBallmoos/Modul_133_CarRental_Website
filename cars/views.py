from django.shortcuts import render, redirect
from .models import Cars
"""from .forms import AuthorForm, BookForm"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def cars(request):
    return render(request, 'functions/show_cars.html')


def show_cars(request, cars_id):
    try:
        cars = Cars.objects.get(pk=cars_id)
    except Cars.DoesNotExist:
        messages.error(request, 'There is no car with this id!')
        return redirect(list_cars)
    form = AuthorForm(initial={
        'first_name': cars.first_name,
        'last_name': cars.last_name,
    })
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=cars)
        if form.is_valid():
            cars.first_name = form.cleaned_data['first_name']
            cars.last_name = form.cleaned_data['last_name']
            cars.image = form.cleaned_data['image']
            cars.save()
        messages.success(request, 'Author successfully updated')
    return render(request, 'functions/show_cars.html', {'cars': cars, 'form': form})
