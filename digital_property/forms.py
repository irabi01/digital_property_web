from django import forms
from .models import Land, House

class LandForm(forms.ModelForm):
    class Meta:
        model = Land
        fields = ['Title','Location','Area','Image','Price','Description']
        widgets = {
            'Title': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Enter property title','value':'Land'}),
            'Price': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Enter property price'}),
            'Area': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Area in sq. meter'}),
            'Image': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'paste image url'}),
        }

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['Title','Location','Type','Number_of_bedrooms','Image','Price','Description']
        widgets = {
            'Title': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter property title','value':'House'}),
            'Price': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Enter property price'}),
            'Image': forms.TextInput(attrs = {'class':'form-control','placeholder':'paste image url'}),
        }
