from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


def home(request):
    return render(request, 'base_home/home.html')


def signup(request):
    return render(request, 'registration/signup.html')


def login(request):
    return render(request, 'registration/login.html')








