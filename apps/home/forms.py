from django import forms 


class ExcelForm(forms.Form):
    file=forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )
        
    )