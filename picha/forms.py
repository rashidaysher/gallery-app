from django import forms
from django.forms import ModelForm
from .models import *

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

CATEGORIES =( 
    ("1", "Cars"), 
    ("2", "Food"), 
    ("3", "Travel"),   
    ("4", "Animals"), 
    ("5", "Nature"), 
    ("6", "Sports"), 
) 

class ImagesForm(forms.Form):
    image = forms.ImageField(required=True) 
    imagename = forms.CharField(required=True)
    description = forms.CharField(required=True)
    locaton = forms.CharField(required=True)
    category = forms.ChoiceField(choices=CATEGORIES, required=True)