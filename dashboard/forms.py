from django import forms
from .models import *

class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('name', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control my-3 city-input w-75 mx-auto','placeholder': 'Enter City Name...'})
        }