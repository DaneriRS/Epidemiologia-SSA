from django import forms 
from django.forms import ModelForm
from apps.home.models import *
from django.contrib.auth.models import User, Group

MUNICIPIOS =(
    ("1", "MORELIA"),
    ("2", "LA ALDEA")
)    

INSTITUCION =(
    ("1", "SSA"),
    ("2", "ISSSTE")
)      
JUROEQUI = (
    ("1", "LA ALDEA"),
    ("2", "MORELIA")
)
TIPOHEP = (
    ("1", "A"),
    ("2", "B"),
    ("3", "C"),
    ("4", "D"),
    ("5", "E")
)
GENERO = (
    ("1", "MASCULINO"),
    ("2", "FEMENINO")
)

class registroPaciente(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'nacimiento' : forms.DateInput(attrs={'type' : 'date'})
         }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'required': 'required'
            })
class ContactForm1(forms.Form):
    folio = forms.CharField(
        max_length=20,
        label="Folio:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control',
            }
        )
    )
    unidadNot = forms.CharField(
        max_length=20,
        label="Unidad notificante:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    local = forms.CharField(
        max_length=20,
        label="Localidad:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    entOdEL = forms.CharField(
        max_length=20,
        label="Entidad o delegacion:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    cvClue = forms.CharField(
        max_length=20,
        label="Clave CLUES:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    municipio1 = forms.ChoiceField(
        choices = MUNICIPIOS,
        label = 'Municipio: ',
        widget = forms.Select(
            attrs={'class': 'form-control '}
        )
    )
    institucion = forms.ChoiceField(
        choices = INSTITUCION,
        label = 'Institucion: ',
        widget = forms.Select(
            attrs={'class': 'form-control '}
        )
    )
    cvSuUni = forms.CharField(
        max_length=20,
        label="Clave suave de la unidad:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    jurisdicEq = forms.ChoiceField(
        choices = JUROEQUI,
        label = 'Jurisdiccion o equivalente: ',
        widget = forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        )
    )
    fechaNot = forms.CharField(
        label = 'Fecha de creacion',
        widget=forms.DateInput(
            format='%YYYY-%MM-%DD',
            attrs={
                'class': 'form-control', 'type': 'date',
                'data-target': '#datetimepicker1'
            }
        )
    )
    fechaIni = forms.CharField(
        label = 'Inicio de estudio: ',
        widget=forms.DateInput(
            format='%YYYY-%MM-%DD',
            attrs={
                'class': 'form-control', 'type': 'date',
                'data-target': '#datetimepicker1'
            }
        )
    )
    fechaFin = forms.CharField(
        label = 'Terminacion de estudio: ',
        widget=forms.DateInput(
            format='%YYYY-%MM-%DD',
            attrs={
                'class': 'form-control', 'type': 'date',
                'data-target': '#datetimepicker1'
            }
        )
    )
    DiaProHep = forms.ChoiceField(
        choices = TIPOHEP,
        label = 'Diagnostico probable de hepatitis: ',
        widget = forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        )
    )
    DiaFin = forms.ChoiceField(
        choices = TIPOHEP,
        label = 'Diagnostico final: ',
        widget = forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        )
    )
    otroDia = forms.CharField(
        max_length=20,
        label="Otro diagnostico:",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Especificar nombre de la enfermedad', 'class': 'form-control'
            }
        )
    )


class ContactForm2(forms.Form):
    noAfili = forms.CharField(
        max_length=30,
        label="Num, de afiliacion o expediente: ",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    nombre = forms.CharField(
        max_length=30,
        label="Nombre(s): ",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    ap = forms.CharField(
        max_length=30,
        label="Apellido paterno: ",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    am = forms.CharField(
        max_length=30,
        label="Apellido materno: ",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    sexo = forms.ChoiceField(
        choices = GENERO,
        label = 'Genero: ',
        widget = forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        )
    )
    fechaNac = forms.CharField(
        label = 'Fecha de nacimiento: ',
        widget=forms.DateInput(
            format='%YYYY-%MM-%DD',
            attrs={
                'class': 'form-control', 'type': 'date',
                'data-target': '#datetimepickerFechaNac'
            }
        )
    )
    anos = forms.IntegerField(
        label='Años: ',
         widget = forms.NumberInput(
            attrs={
                'class': 'form-control', 'min': '0', 'max': '120'
            }
        )
    )
    meses = forms.IntegerField(
        label='Meses: ',
         widget = forms.NumberInput(
            attrs={
                'class': 'form-control', 'min': '0', 'max': '13'
            }
        )
    )
    dias = forms.IntegerField(
        label='Dias: ',
         widget = forms.NumberInput(
            attrs={
                'class': 'form-control', 'min': '0', 'max': '32'
            }
        )
    )
    calle = forms.CharField(
        max_length=50,
        label="Calle: ",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    num = forms.CharField(
        max_length=10,
        label="Numero interior y/o exterior: ",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    colonia = forms.CharField(
        max_length=50,
        label="Colonia o localidad: ",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    municipio2 = forms.ChoiceField(
        choices = MUNICIPIOS,
        label = 'Municipio: ',
        widget = forms.Select(
            attrs={'class': 'form-control '}
        )
    )
    cvMun2 = forms.CharField(
        max_length=3,
        label="Clave: ",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    ent2 = forms.CharField(
        max_length=20,
        label="Entidad:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    cvEnt2 = forms.CharField(
        max_length=2,
        label="Clave: ",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    cp2 = forms.CharField(
        max_length=5,
        label="CP: ",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    tel2 = forms.CharField(
        max_length=15,
        label="Telefono: ",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

class ContactForm3(forms.Form):
    fechaIn3 = forms.CharField(
        label = 'Fecha de inicio de signos: ',
        widget=forms.DateInput(
            format='%YYYY-%MM-%DD',
            attrs={
                'class': 'form-control', 'type': 'date',
                'data-target': '#datetimepickerFechaIn3'
            }
        )
    )

    signoSint3 = forms.CharField(
        label="Signos y sintomas: ",
        max_length=200,
        widget=forms.Textarea(
            attrs={'placeholder': 'Describe los signos y sintomas','class': 'form-control'}
        )
    )

    tratamiento3 = forms.CharField(
        label="Describa el tratamiento",
        max_length=200,
        widget=forms.Textarea(
            attrs={'placeholder': 'Describa el tratamiento', 'class': 'form-control'}
        )
    )
