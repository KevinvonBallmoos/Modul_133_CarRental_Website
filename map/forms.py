from django import forms
from .models import Map


class MapForm(forms.ModelForm):
    """
    loads class Map
    """
    class Meta:
        model = Map
        fields = '__all__'

