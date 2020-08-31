from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


def home(request):
    return render(request, 'base_home/home.html')


def signup(request):
    return render(request, 'registration/signup.html')


def signin(request):
    return render(request, 'registration/signin.html')


def cars(request):
    return render(request, 'functions/cars.html')


def map(request):
    return render(request, 'functions/map.html')





