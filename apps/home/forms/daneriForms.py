from django import forms 
from django.forms import ModelForm
from apps.home.models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import permission_required

class actualizaPerfil(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'User': 'username'})
        self.fields['email'].widget.attrs.update({'User': 'email'})
        self.fields['password'].widget.attrs.update({'User': 'password'})
        self.fields['first_name'].widget.attrs.update({'User': 'firstname'})
        self.fields['last_name'].widget.attrs.update({'User': 'last_name'})
        self.fields['groups'].widget.attrs.update({'CustomUser': 'User'})


class userProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autofocus'] = True

    class Meta:
        _model = User
        fields = 'username', 'password', 'email', 'first_name', 'last_name',
        widgets = {
            'username': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',})),
            'password': forms.PasswordInput(attrs={'class': 'form-control',}                                ),
            'email': forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',})),
            'first_name': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',})),
            'last_name': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',})),
        }

class addEstablecimiento(ModelForm):
    
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

class addEntidad(ModelForm):

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
