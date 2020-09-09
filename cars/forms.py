from django import forms
from .models import Cars

""" lädt die Formen für Create, Update, Delete
"""


class CarForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'


