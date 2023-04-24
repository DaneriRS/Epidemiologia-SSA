from django import forms 
from django.forms import ModelForm
from apps.home.models import *
from django.contrib.auth.models import User, Group
        
class GroupAssignForm(forms.ModelForm):
    groups = forms.MultipleChoiceField(
        choices=[(group.id, group.name) for group in Group.objects.all()],
        widget=forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
        required=False
    )
    
    class Meta:
        model = User
        fields = ['groups']
        
class InformacionUsuarioForm(forms.ModelForm):
    
    class Meta:
        model = InformacionUsuario
        fields = ['unidad', 'jurisdiccion']
        labels = {
            'unidad': 'Unidad',
            'jurisdiccion': 'Jurisdiccion'
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Ordenar las opciones de "unidad" y "jurisdiccion" de forma alfabética
        self.fields['unidad'].queryset = self.fields['unidad'].queryset.order_by('claveclues')
        self.fields['jurisdiccion'].queryset = self.fields['jurisdiccion'].queryset.order_by('clave')
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            
class MunicipioForm(forms.ModelForm):
    
    class Meta:
        model = Municipio
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields[field].required = True
            
class LocalidadForm(forms.ModelForm): 
    
    class Meta:
        model = Localidad
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields[field].required = True
            
class TipologiaForm(forms.ModelForm):
    
    class Meta:
        model = Tipologia
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields[field].required = True

class JurisdiccionForm(forms.ModelForm):
    
    class Meta:
        model = Jurisdiccion
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields[field].required = True

class InstitucionForm(forms.ModelForm):
    
    class Meta:
        model = Institucion
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields[field].required = True