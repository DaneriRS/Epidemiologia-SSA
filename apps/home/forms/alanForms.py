from django import forms 
from django.forms import ModelForm
from apps.home.models import *
from django.contrib.auth.models import User, Group

# class GroupAssignForm(forms.ModelForm):
#     groups = forms.ModelMultipleChoiceField(
#         queryset=Group.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=False
#     )
    
#     class Meta:
#         model = User
#         fields = ['groups']
        
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