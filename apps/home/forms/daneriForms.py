from django import forms
from django.conf import settings
from django.forms import ModelForm
from apps.home.models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import permission_required
from os import *
from tkinter import *
from PIL import ImageTk, Image


class userProfileform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
      #  self.fields['username'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'username', 'email', 'first_name', 'last_name',
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',}),
            'email': forms.EmailInput(attrs={'class': 'form-control',}),
            'first_name': forms.TextInput(attrs={'class': 'form-control',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',}),
        }

class EntidadForm(ModelForm):
    class Meta:
        model = Entidad
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'required': 'required'
            })

class EstablecimientoForm(ModelForm):
    class Meta:
        model = Establecimiento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'required': 'required'
            })


class LogosForm(forms.ModelForm):
    #logosAll = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Logos
        fields = '__all__'

    def resize(logo,new_height):
        carpeta_logos = os.path.dirname('logos.urls')
        logos_names = os.listdir(carpeta_logos)

        for logos_names in logos_names:
            if logos_names.split(".")[-1] not in ["png"]:
                continue
            image_path = carpeta_logos + "/" + logos_names
            imagenLogo = ImageTk.PhotoImage(Image.open(image_path).resize((0,85), Image.ANTIALIAS))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'required': 'required'
            })
