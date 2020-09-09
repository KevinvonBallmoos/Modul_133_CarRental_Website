from django import forms
from .models import Map

""" lädt die Formen für Create, Update, Delete
"""


class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = '__all__'

