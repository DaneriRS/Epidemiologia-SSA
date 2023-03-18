from django import forms 
from django.forms import ModelForm
from apps.home.models import *
from django.contrib.auth.models import User, Group

class User(forms.Form):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            '' : forms.TextInput(attrs={'class' : 'form-control'})
         }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'required': 'required'
            })

class unidadPerfil(forms.Form):
    class Meta:
        model = models.Model
        fields = 'unidad', 'claveclues','jurisdiccion','municipio','entidad'
        widgets = {
            '' : forms.TextInput(attrs={'class' : 'form-control'})
         }
    