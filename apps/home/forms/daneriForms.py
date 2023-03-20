from django import forms 
from django.forms import ModelForm
from apps.home.models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import permission_required

class User(forms.Form):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            '' : forms.TextInput(attrs=(['class']=: 'form-control'))
        }
        permissions_required='User.can_edit'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'required': 'required'
            })
        for form in self.visible_fields():
                form.field.widget.attrs['class']= 'form-control',
                form.field.widget.attrs['autocomplete']= 'off',


class actualizaPerfil(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'User': 'username'})
        self.fields['email'].widget.attrs.update({'User': 'email'})
        self.fields['password'].widget.attrs.update({'User': 'password'})
        self.fields['first_name'].widget.attrs.update({'User': 'firstname'})
        self.fields['last_name'].widget.attrs.update({'User': 'last_name'})
        self.fields['unidad'].widget.attrs.update({'Institucion': 'nombre'})
        self.fields['claveClues'].widget.attrs.update({'unidad': 'claveclues'})
        self.fields['jurisdiccion'].widget.attrs.update({'jurisdiccion': 'clave'})
        self.fields['municipio'].widget.attrs.update({'Municipio': 'nombre'})
        self.fields['entidad'].widget.attrs.update({'Entidad': 'nombre'})
        self.fields['groups'].widget.attrs.update({'CustomUser': 'User'})

