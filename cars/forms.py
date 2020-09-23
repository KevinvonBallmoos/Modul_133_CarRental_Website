from django import forms
from .models import Cars, CarTypes


class CarForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'


class CarTypeForm(forms.ModelForm):
    class Meta:
        model = CarTypes
        fields = '__all__'
