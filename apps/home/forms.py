from django import forms 


class ExcelForm(forms.Form):
    Subir_Excel=forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )  
    )

class IndividualForm(forms.Form):
    Usuario=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )  
    )
    Nombre=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )  
    )
    Apellidos=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )  
    )
    Correo=forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control'
            }
        )  
    )
    Contraseña=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )  
    )