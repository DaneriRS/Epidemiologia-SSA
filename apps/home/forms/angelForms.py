from django import forms 
from django.forms import ModelForm
from apps.home.models import *
from django.contrib.auth.models import User, Group
from django.forms import formset_factory

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
    unidadNot = forms.ModelChoiceField(
        queryset=Unidad.objects.all(),
        label='Unidad notificante:',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'readonly': True
            }
        ),
        required=True
    )
    fechaNot = forms.DateField(
        label = 'Fecha de creacion',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        ),
        required=True
    )
    fechaIni = forms.DateField(
        label = 'Inicio de estudio: ',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        ),
        required=True
    )
    fechaFin = forms.DateField(
        label = 'Terminacion de estudio: ',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        )
    )
    DiaProHep = forms.ChoiceField(
        choices = HEPATITIS_CHOICES,
        label = 'Diagnostico probable de hepatitis: ',
        widget = forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        ),
        required=True
    )
    DiaFin = forms.ChoiceField(
        choices = HEPATITIS_CHOICES,
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
    paciente = forms.ModelChoiceField(
        label="Num, de afiliacion o expediente: ",
        queryset=Paciente.objects.all(),
        widget=forms.Select(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

class ContactForm3(forms.Form):
    fechaIn3 = forms.DateField(
        label = 'Fecha de inicio de signos: ',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date'
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

class ContactoForm4(forms.Form):
    nombre = forms.CharField(
        max_length=30,
        label="Estudio",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control',
            }
        )
    )
    tipo = forms.CharField(
        max_length=30,
        label="Tipo",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    fecha = forms.CharField(
        label = 'Fecha: ',
        widget=forms.DateInput(
            format='%YYYY-%MM-%DD',
            attrs={
                'class': 'form-control', 'type': 'date',
                'data-target': '#datetimepickerfechaEstudio'
            }
        )
    )
    resultado = forms.CharField(
        max_length=30,
        label="Resultado: ",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        ),
        required=False
    )

class ContactoForm5(forms.Form):
    id = forms.CharField(
        max_length=30,
        label="Id",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control',
                'hidden': 'true'
            }
        ),
        required=False,
    )
    nombre = forms.CharField(
        max_length=30,
        label="Estudio",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control',
            }
        )
    )
    tipo = forms.CharField(
        max_length=30,
        label="Tipo",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    fecha = forms.CharField(
        label = 'Fecha: ',
        widget=forms.DateInput(
            format='%YYYY-%MM-%DD',
            attrs={
                'class': 'form-control', 'type': 'date',
                'data-target': '#datetimepickerfechaEstudio'
            }
        )
    )
    resultado = forms.CharField(
        max_length=30,
        label="Resultado: ",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        ),
        required=False
    )

class NotificacionBrote1(forms.Form):
    unidadNot = forms.ModelChoiceField(
        queryset=Unidad.objects.all(),
        label='Unidad notificante:',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'readonly': True
            }
        ),
        required=True
    )
    fechaNot = forms.CharField(
        label = 'Fecha de Notificacion',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        )
    )
    fechaEstudio = forms.CharField(
        label = 'Inicio de estudio: ',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        )
    )
    DiaProHep = forms.ChoiceField(
        choices = HEPATITIS_CHOICES,
        label = 'Diagnostico probable de hepatitis: ',
        widget = forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        )
    )
    DiaFin = forms.ChoiceField(
        choices = HEPATITIS_CHOICES,
        label = 'Diagnostico final: ',
        widget = forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        )
    )

class NotificacionBrote2(forms.Form):
    DiaProHep2 = forms.ChoiceField(
        choices = HEPATITIS_CHOICES,
        label = 'Diagnostico probable de hepatitis: ',
        widget = forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        )
    )
    DiaFin2 = forms.ChoiceField(
        choices = HEPATITIS_CHOICES,
        label = 'Diagnostico final: ',
        widget = forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        )
    )
    fechaNot2 = forms.CharField(
        label = 'Fecha de Notificacion',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        )
    )
    fechaNot3 = forms.CharField(
        label = 'Inicio de estudio: ',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        )
    )
    casosProbables = forms.CharField(
        max_length=4,
        label="Casos Probables:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    casosConfirmados = forms.CharField(
        max_length=4,
        label="Casos Confirmados:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    hospitalizados = forms.CharField(
        max_length=4,
        label="Hospitalizados:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    
class NotificacionBrote5(forms.Form):
    area = forms.CharField(
        max_length=20,
        label="Area:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        ),
        required=True
    )
    numeroCasos = forms.CharField(
        max_length=20,
        label="Casos:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    numeroDefunciones = forms.CharField(
        max_length=20,
        label="Defunciones:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

class NotificacionBrote6(forms.Form):
    anteEpiBrote = forms.CharField(
        max_length=20,
        label="Antecedentes epidemiológicos del brote:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    probFuenBrote = forms.CharField(
        max_length=20,
        label="Probables fuentes del brote:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    probMecTransmision = forms.CharField(
        max_length=20,
        label="Probables mecanismos de transmisión:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

class NotificacionBrote7(forms.Form):
    accionesPrevControl = forms.CharField(
        max_length=200,
        label="Acciones de prevención y control realizadas:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

class NotificacionBrote8(forms.Form):
    id = forms.CharField(
        max_length=20,
        label="Area:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control',
                'hidden': 'true'
            }
        )
    )
    area = forms.CharField(
        max_length=20,
        label="Area:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    numeroCasos = forms.CharField(
        max_length=20,
        label="Casos:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    numeroDefunciones = forms.CharField(
        max_length=20,
        label="Defunciones:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

class Anexo8P1(forms.Form):
    nombreFallecido = forms.ModelChoiceField(
        queryset=Paciente.objects.all(),
        label='Nombre del Fallecido:',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        required=True
    )
    institucion = forms.ModelChoiceField(
        queryset=Institucion.objects.all(),
        label='Institución:',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        required=True
    )
    fechaDefuncion = forms.CharField(
        label = 'Fecha de Defuncion',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        )
    )
    escolaridad = forms.ChoiceField(
        choices = ESCOLARIDAD_CHOICES,
        label = 'Escolaridad: ',
        widget = forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        )
    )
    ocupacion = forms.CharField(
        max_length=20,
        label="Ocupacion:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    lugardeResidenciaMuni = forms.ModelChoiceField(
        queryset=Municipio.objects.all(),
        label='Lugar de Residencia Habitual (Municipio):',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        required=True
    )
    lugardeResidenciaEnti = forms.ModelChoiceField(
        queryset=Entidad.objects.all(),
        label='Lugar de Residencia Habitual (Entidad Federativa):',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        required=True
    )
    lugarDefMuni = forms.ModelChoiceField(
        queryset=Municipio.objects.all(),
        label='Lugar de Donde Ocurrio la Defunsion (Municipio):',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        required=True
    )
    lugarDefEnti = forms.ModelChoiceField(
        queryset=Entidad.objects.all(),
        label='Lugar de Donde Ocurrio la Defunsion (Entidad Federativa):',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        required=True
    )
    nombreCertificante = forms.CharField(
        max_length=20,
        label="Nombre del Certificante:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

class Anexo8P2(forms.Form):
    causasDef = forms.CharField(
        max_length=100,
        label="I:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    causasDef2 = forms.CharField(
        max_length=100,
        label="II:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    causaVigEpi = forms.CharField(
        max_length=100,
        label="Causa sujeta a vigilancia epidemiologica:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

class addJurisdiccion(ModelForm):
    
    class Meta:
        model = Jurisdiccion
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'required': 'required'
            })
