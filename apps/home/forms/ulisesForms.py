from django import forms 
from django.forms import ModelForm
from apps.home.models import *
from django.contrib.auth.models import User, Group


class ExcelForm(forms.Form):
    Subir_Excel=forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )  
    )

class ExcelLocalidadForm(forms.Form):
    Subir_LocalidadExcel=forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )  
    )

class ExcelMunicipioForm(forms.Form):
    Subir_MunicipioExcel=forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )  
    )

class ExcelUMedicasForm(forms.Form):
    Subir_UmedicasExcel=forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )  
    )

class IndividualForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }