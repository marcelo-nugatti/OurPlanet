from django import forms
from django.forms import ModelForm

from .models import *

class WeightEarthForm(forms.ModelForm):
    class Meta:
        model = WeightEarth
        fields = '__all__'


