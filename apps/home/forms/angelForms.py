from django import forms
from django.forms import ModelForm
from apps.home.models import *
from django.contrib.auth.models import User, Group
from django.forms import formset_factory

MUNICIPIOS = (
    ("1", "MORELIA"),
    ("2", "LA ALDEA")
)
INSTITUCION = (
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
            'nacimiento': forms.DateInput(attrs={'type': 'date'})
         }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })



class ContactForm1(forms.Form):
    unidadNot = forms.ModelChoiceField(
        label="Unidad notificante:",
        queryset=Unidad.objects.all(),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'readonly':True
            }
        )
    )
    fechaNot = forms.DateField(
        label='Fecha de creacion',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        ),
        required=True
    )
    fechaIni = forms.DateField(
        label='Inicio de estudio: ',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        ),
        required=True
    )
    fechaFin = forms.DateField(
        label='Terminacion de estudio: ',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        ),
        required=False
    )
    DiaProHep = forms.ChoiceField(
        choices=HEPATITIS_CHOICES,
        label='Diagnostico probable de hepatitis: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        ),
        required=True
    )
    DiaFin = forms.ChoiceField(
        choices=HEPATITIS_CHOICES2,
        label='Diagnostico final: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        ),
        required=False
    )
    otroDia = forms.CharField(
        max_length=20,
        label="Otro diagnostico:",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Especificar nombre de la enfermedad', 'class': 'form-control'
            }
        ),
        required=False
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
        label='Fecha de inicio de signos: ',
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
            attrs={'placeholder': 'Describe los signos y sintomas',
                'class': 'form-control'}
        )
    )

    tratamiento3 = forms.CharField(
        label="Describa el tratamiento",
        max_length=200,
        widget=forms.Textarea(
            attrs={'placeholder': 'Describa el tratamiento',
                'class': 'form-control'}
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
    tipo = forms.ChoiceField(
        choices=TIPO_ESTUDIOS_CHOICES,
        label="Tipo",
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        ),
    )
    fecha = forms.DateField(
        label='Fecha: ',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
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
    tipo = forms.ChoiceField(
        choices=TIPO_ESTUDIOS_CHOICES,
        label="Tipo",
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        ),
    )
    fecha = forms.DateField(
        label='Fecha: ',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
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

class ContactoForm6(forms.Form):
    procedencia = forms.ChoiceField(
        choices=PROCEDENCIA_OPCIONES,
        label='Procedencia: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                'onchange': 'procedenciaChanged()'
                }
        ),
        required=True
    )
    municipioProc = forms.ModelChoiceField(
        queryset=Municipio.objects.all(),
        label='Municipio:',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False
    )
    localidadProc = forms.ModelChoiceField(
        queryset=Localidad.objects.all(),
        label='Localidad:',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False
    )
    llegadaProc = forms.DateField(
        label='Llegada:',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        ),
        required=False
    )
    salidaProc = forms.DateField(
        label='Salida:',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        ),
        required=False
    )
    otraPersona = forms.ChoiceField(
        choices=OTRA_PERSONA_OPCIONES,
        label='Otra persona: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
            }
        ),
        required=True
    )
    alimentos = forms.ChoiceField(
        choices=OTRA_PERSONA_OPCIONES,
        label='Alimentos: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
            }

        ),
        required=True
    )
    agua = forms.ChoiceField(
        choices=OTRA_PERSONA_OPCIONES,
        label='Agua: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
            }
        ),
        required=True
    )
    fomites = forms.ChoiceField(
        choices=OTRA_PERSONA_OPCIONES,
        label='Fomites: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
            }
        ),
        required=True
    )
    animales = forms.ChoiceField(
        choices=OTRA_PERSONA_OPCIONES,
        label='Animales: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
            }
        ),
        required=True
    )
    otrosFuentes = forms.CharField(
        max_length=200,
        label='Otras fuentes: ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control ',
            }
        ),
        required=False
    )
    personaPersona = forms.ChoiceField(
        choices=OTRA_PERSONA_OPCIONES,
        label='Persona a persona: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
            }
        ),
        required=True
    )
    aerea = forms.ChoiceField(
        choices=OTRA_PERSONA_OPCIONES,
        label='Aerea: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
            }
        ),
        required=True
    )
    digestiva = forms.ChoiceField(
        choices=OTRA_PERSONA_OPCIONES,
        label='Digestiva: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
            }
        ),
        required=True
    )
    fomitesMec = forms.ChoiceField(
        choices=OTRA_PERSONA_OPCIONES,
        label='Fomites: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
            }
        ),
        required=True
    )
    vectores = forms.ChoiceField(
        choices=OTRA_PERSONA_OPCIONES,
        label='Vectores: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
            }
        ),
        required=True
    )
    otrosMecanismos = forms.CharField(
        max_length=200,
        label='Otras mecanismos: ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control selectpicker',
            }
        ),
        required=False
    )

class ContactoForm7(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        label="Nombre Completo:",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    domicilio = forms.CharField(
        max_length=50,
        label="Domicilio:",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    edad = forms.CharField(
        max_length=20,
        label="Edad:",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    sexo = forms.ChoiceField(
        choices=GENEROS,
        label='Sexo: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
            }
        ),
        required=True
    )
    contacto = forms.ChoiceField(
        choices=CONTACTO_CHOICES,
        label='Contacto: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
            }
        ),
        required=True
    )
    caso = forms.ChoiceField(
        choices=SI_NO_OPCIONES,
        label='Caso: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                'onChange': 'conteoChanged()'
            }
        ),
        required=True
    )
    
class ContactoFormEdit(forms.Form):
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
        max_length=50,
        label="Nombre Completo:",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    domicilio = forms.CharField(
        max_length=50,
        label="Domicilio:",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    edad = forms.CharField(
        max_length=20,
        label="Edad:",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    sexo = forms.ChoiceField(
        choices=GENEROS,
        label='Sexo: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
            }
        ),
        required=True
    )
    contacto = forms.ChoiceField(
        choices=CONTACTO_CHOICES,
        label='Contacto: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
            }
        ),
        required=True
    )
    caso = forms.ChoiceField(
        choices=SI_NO_OPCIONES,
        label='Caso: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                'onChange': 'conteoChanged()'
            }
        ),
        required=True
    )
    
class ContactoForm8(forms.Form):
    accionesMedidas = forms.CharField(
        max_length=300,
        label='Acciones y medidas de control: ',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control ',
            }
        ),
        required=True
    )

class ContactoForm9(forms.Form):
    reestablecer = forms.ChoiceField(
        choices=SI_NO_OPCIONES2,
        label='¿Se restableció integramente?: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control ',
            }
        ),
        required=False
    )
    secuelas = forms.ChoiceField(
        choices=SI_NO_OPCIONES2,
        label='¿Quedó con secuelas?: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
            }
        ),
        required=False
    )
    portador = forms.ChoiceField(
        choices=SI_NO_OPCIONES2,
        label='¿Quedó como portador?: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
            }
        ),
        required=False
    )
    perdioCaso = forms.ChoiceField(
        choices=SI_NO_OPCIONES2,
        label='¿Se perdió el caso?: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
            }
        ),
        required=False
    )
    fallecio = forms.ChoiceField(
        choices=SI_NO_OPCIONES2,
        label='¿Falleció?: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                'onchange': 'fallecioChanged()'
            }
        ),
        required=False
    )
    fechaDefuncion = forms.DateField(
        label='Fecha de la defunción:',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        ),
        required=False
    )

class ContactoForm10(forms.Form):
    platicas = forms.ChoiceField(
        choices=SI_NO_OPCIONES,
        label='Platicas de fomento para la salud: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                'onChange': 'ejecutar()',
            }
        ),
        required=True
    )
    numPlaticas = forms.CharField(
        label='Numero de platicas: ',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control ',
                'min': 0,
            }
        ),
        required=False
    )
    vacunacion = forms.ChoiceField(
        choices=SI_NO_OPCIONES,
        label='Vacunación: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                'onChange': 'ejecutar()',
            }
        ),
        required=True
    )
    numVacunacion = forms.CharField(
        label='Numero de vacunacion: ',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control ',
                'min': 0,
            }
        ),
        required=False
    )
    tratamientosInd = forms.ChoiceField(
        choices=SI_NO_OPCIONES,
        label='Tratamientos individuales: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                'onChange': 'ejecutar()',
            }
        ),
        required=True
    )
    numTratamientosInd = forms.CharField(
        label='Numero de tratamientos individuales: ',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control ',
                'min': 0,
            }
        ),
        required=False
    )
    tratamientosFam = forms.ChoiceField(
        choices=SI_NO_OPCIONES,
        label='Tratamientos familiares: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                'onChange': 'ejecutar()',
            }
        ),
        required=True
    )
    numTratamientosFam = forms.CharField(
        label='Numero de tratamientos familiares: ',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control ',
                'min': 0,
            }
        ),
        required=False
    )
    cloracion = forms.ChoiceField(
        choices=SI_NO_OPCIONES,
        label='Cloración: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                'onChange': 'ejecutar()',
            }
        ),
        required=True
    )
    numCloracion = forms.CharField(
        label='Numero cloracion: ',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control ',
                'min': 0,
            }
        ),
        required=False
    )
    letrinizacion = forms.ChoiceField(
        choices=SI_NO_OPCIONES,
        label='Letrinización: ',
        widget=forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                'onChange': 'ejecutar()',
            }
        ),
        required=True
    )
    numLetrinizacion = forms.CharField(
        label='Numero letrinizacion: ',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control ',
                'min': 0,
            }
        ),
        required=False
    )
    otrasActividades = forms.CharField(
        label='Otras actividades: ',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control ',
            }
        ),
        required=False
    )

class ContactoForm11(forms.Form):
    comentariosConclusiones = forms.CharField(
        max_length=300,
        label='Comentarios y conclusiones: ',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control ',
            }
        ),
        required=True
    )




class NotificacionBrote1(forms.Form):
    unidadNot = forms.ModelChoiceField(
        queryset = Unidad.objects.all(),
        label = 'Unidad notificante:',
        widget = forms.Select(
            attrs={
                'class': 'form-control',
                'readonly': True
            }
        ),
        required = True
    )
    fechaNot=forms.CharField(
        label = 'Fecha de Notificacion',
        widget = forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        )
    )
    fechaEstudio=forms.CharField(
        label = 'Inicio de estudio: ',
        widget = forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        )
    )
    DiaProHep=forms.ChoiceField(
        choices = HEPATITIS_CHOICES,
        label = 'Diagnostico probable de hepatitis: ',
        widget = forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        )
    )
    DiaFin=forms.ChoiceField(
        choices = HEPATITIS_CHOICES,
        label = 'Diagnostico final: ',
        widget = forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        )
    )

class NotificacionBrote2(forms.Form):
    DiaProHep2=forms.ChoiceField(
        choices = HEPATITIS_CHOICES,
        label = 'Diagnostico probable de hepatitis: ',
        widget = forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        )
    )
    DiaFin2=forms.ChoiceField(
        choices = HEPATITIS_CHOICES,
        label = 'Diagnostico final: ',
        widget = forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        )
    )
    fechaNot2=forms.CharField(
        label = 'Fecha de Notificacion',
        widget = forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        )
    )
    fechaNot3=forms.CharField(
        label = 'Inicio de estudio: ',
        widget = forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        )
    )
    casosProbables=forms.CharField(
        max_length = 4,
        label = "Casos Probables:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    casosConfirmados=forms.CharField(
        max_length = 4,
        label = "Casos Confirmados:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    hospitalizados=forms.CharField(
        max_length = 4,
        label = "Hospitalizados:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

class NotificacionBrote5(forms.Form):
    area=forms.CharField(
        max_length = 20,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        ),
        required = True
    )
    numeroCasos=forms.CharField(
        max_length = 20,
        label = "Casos:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    numeroDefunciones=forms.CharField(
        max_length = 20,
        label = "Defunciones:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

class NotificacionBrote6(forms.Form):
    anteEpiBrote=forms.CharField(
        max_length = 20,
        label = "Antecedentes epidemiológicos del brote:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    probFuenBrote=forms.CharField(
        max_length = 20,
        label = "Probables fuentes del brote:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    probMecTransmision=forms.CharField(
        max_length = 20,
        label = "Probables mecanismos de transmisión:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

class NotificacionBrote7(forms.Form):
    accionesPrevControl=forms.CharField(
        max_length = 200,
        label = "Acciones de prevención y control realizadas:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

class NotificacionBrote8(forms.Form):
    id=forms.CharField(
        max_length = 20,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control',
                'hidden': 'true'
            }
        )
    )
    area=forms.CharField(
        max_length = 20,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    numeroCasos=forms.CharField(
        max_length = 20,
        label = "Casos:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    numeroDefunciones=forms.CharField(
        max_length = 20,
        label = "Defunciones:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )


class NotificacionBrote3(forms.Form):
    #### Numero de Casos
    menor1MascNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    menor1FemNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    menor1TotNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de14MascNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de14FemNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de14TotNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de59MascNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de59FemNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de59TotNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1014MascNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1014FemNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1014TotNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1519MascNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1519FemNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1519TotNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2024MascNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2024FemNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2024TotNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2544MascNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2544FemNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2544TotNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de4549MascNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de4549FemNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de4549TotNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de5059MascNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de5059FemNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de5059TotNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de6064MascNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de6064FemNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de6064TotNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    mas65MascNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    mas65FemNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    mas65TotNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    seIgnoraMascNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    seIgnoraFemNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    seIgnoraTotNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    totalMascNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    totalFemNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    totalTotNumerosCasos=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    
    #### Numero de Defunciones
    menor1MascNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    menor1FemNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    menor1TotNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de14MascNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de14FemNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de14TotNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de59MascNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de59FemNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de59TotNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1014MascNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1014FemNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1014TotNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1519MascNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1519FemNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1519TotNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2024MascNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2024FemNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2024TotNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2544MascNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2544FemNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2544TotNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de4549MascNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de4549FemNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de4549TotNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de5059MascNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de5059FemNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de5059TotNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de6064MascNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de6064FemNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de6064TotNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    mas65MascNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    mas65FemNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    mas65TotNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    seIgnoraMascNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    seIgnoraFemNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    seIgnoraTotNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    totalMascNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    totalFemNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    totalTotNumerosDefunciones=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

    #### Poblacion Ex

    menor1MascPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    menor1FemPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    menor1TotPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de14MascPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de14FemPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de14TotPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de59MascPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de59FemPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de59TotPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1014MascPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1014FemPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1014TotPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1519MascPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1519FemPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1519TotPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2024MascPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2024FemPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2024TotPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2544MascPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2544FemPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2544TotPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de4549MascPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de4549FemPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de4549TotPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de5059MascPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de5059FemPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de5059TotPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de6064MascPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de6064FemPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de6064TotPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    mas65MascPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    mas65FemPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    mas65TotPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    seIgnoraMascPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    seIgnoraFemPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    seIgnoraTotPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    totalMascPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    totalFemPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    totalTotPoblacionExpuesta=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

    #### Tasa Ataque
    menor1MascTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    menor1FemTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    menor1TotTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de14MascTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de14FemTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de14TotTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de59MascTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de59FemTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de59TotTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1014MascTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1014FemTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1014TotTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1519MascTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1519FemTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1519TotTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2024MascTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2024FemTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2024TotTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2544MascTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2544FemTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2544TotTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de4549MascTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de4549FemTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de4549TotTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de5059MascTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de5059FemTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de5059TotTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de6064MascTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de6064FemTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de6064TotTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    mas65MascTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    mas65FemTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    mas65TotTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    seIgnoraMascTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    seIgnoraFemTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    seIgnoraTotTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    totalMascTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    totalFemTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    totalTotTasaAtaque=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

    #### Tasa Letalidad
    menor1MascTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    menor1FemTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    menor1TotTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de14MascTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de14FemTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de14TotTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de59MascTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de59FemTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de59TotTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1014MascTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1014FemTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1014TotTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1519MascTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1519FemTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1519TotTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2024MascTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2024FemTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2024TotTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2544MascTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2544FemTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2544TotTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de4549MascTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de4549FemTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de4549TotTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de5059MascTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de5059FemTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de5059TotTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de6064MascTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de6064FemTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de6064TotTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    mas65MascTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    mas65FemTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    mas65TotTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    seIgnoraMascTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    seIgnoraFemTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    seIgnoraTotTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    totalMascTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    totalFemTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    totalTotTasaLetalidad=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

    #### Signos y Sintomas
    menor1SignosSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    menor1NumSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    menor1PorcSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de14SignosSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de14NumSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de14PorcSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de59SignosSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de59NumSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de59PorcSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1014SignosSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1014NumSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1014PorcSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1519SignosSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1519NumSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de1519PorcSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2024SignosSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2024NumSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2024PorcSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2544SignosSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2544NumSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de2544PorcSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de4549SignosSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de4549NumSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de4549PorcSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de5059SignosSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de5059NumSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de5059PorcSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de6064SignosSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de6064NumSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    de6064PorcSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    mas65SignosSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    mas65NumSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    mas65PorcSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    seIgnoraSignosSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    seIgnoraNumSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    seIgnoraPorcSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    totalSignosSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    totalNumSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    totalPorcSignosSintomas=forms.CharField(
        max_length = 3,
        label = "Area:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

class Anexo8P1(forms.Form):
    nombreFallecido=forms.ModelChoiceField(
        queryset = Paciente.objects.all(),
        label = 'Nombre del Fallecido:',
        widget = forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        required = True
    )
    institucion=forms.ModelChoiceField(
        queryset = Institucion.objects.all(),
        label = 'Institución:',
        widget = forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        required = True
    )
    fechaDefuncion=forms.CharField(
        label = 'Fecha de Defuncion',
        widget = forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        )
    )
    escolaridad=forms.ChoiceField(
        choices = ESCOLARIDAD_CHOICES,
        label = 'Escolaridad: ',
        widget = forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        )
    )
    ocupacion=forms.CharField(
        max_length = 20,
        label = "Ocupacion:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    lugardeResidenciaMuni=forms.ModelChoiceField(
        queryset = Municipio.objects.all(),
        label = 'Lugar de Residencia Habitual (Municipio):',
        widget = forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        required = True
    )
    lugardeResidenciaEnti=forms.ModelChoiceField(
        queryset = Entidad.objects.all(),
        label = 'Lugar de Residencia Habitual (Entidad Federativa):',
        widget = forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        required = True
    )
    lugarDefMuni=forms.ModelChoiceField(
        queryset = Municipio.objects.all(),
        label = 'Lugar de Donde Ocurrio la Defunsion (Municipio):',
        widget = forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        required = True
    )
    lugarDefEnti=forms.ModelChoiceField(
        queryset = Entidad.objects.all(),
        label = 'Lugar de Donde Ocurrio la Defunsion (Entidad Federativa):',
        widget = forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        required = True
    )
    nombreCertificante=forms.CharField(
        max_length = 20,
        label = "Nombre del Certificante:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

class Anexo8P2(forms.Form):
    causasDef=forms.CharField(
        max_length = 100,
        label = "I:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    causasDef2=forms.CharField(
        max_length = 100,
        label = "II:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    causaVigEpi=forms.CharField(
        max_length = 100,
        label = "Causa sujeta a vigilancia epidemiologica:",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

class Anexo8P3(forms.Form):
    ratifica=forms.CharField(
        max_length = 100,
        label = "Ratifica",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    causaVigEpi2=forms.CharField(
        max_length = 100,
        label = "Causa sujeta a vigilancia epidemiologica",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    causasDef3=forms.CharField(
        max_length = 100,
        label = "Causas de defunción3",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    causasDef4=forms.CharField(
        max_length = 100,
        label = "Causas de defunción4",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    fechaRecoleccion=forms.CharField(
        label = 'Fecha de recolección',
        widget = forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        )
    )
    fechaInicio=forms.CharField(
        label = 'Fecha de inicio',
        widget = forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        )
    )
    fechaConclusion=forms.CharField(
        label = 'Fecha de conclusión',
        widget = forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        )
    )
    reporteInegi=forms.CharField(
        label = 'Fecha de reporte a INEGI',
        widget = forms.DateInput(
            attrs={
                'class': 'form-control', 'type': 'date',
            }
        )
    )
    observaciones=forms.CharField(
        max_length = 100,
        label = "Observaciones",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    nombreResponsableInv=forms.CharField(
        max_length = 100,
        label = "Nombre del responsable de la investigación",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    cargo=forms.CharField(
        max_length = 100,
        label = "Cargo",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    firma=forms.CharField(
        max_length = 100,
        label = "Firma",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

class Anexo8P4(forms.Form):
    tipoDocumento=forms.CharField(
        max_length = 100,
        label = "Tipo de documento",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    numPaquete=forms.CharField(
        max_length = 100,
        label = "Número de paquete",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    numActa=forms.CharField(
        max_length = 100,
        label = "Número de acta",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    folioCaptura=forms.CharField(
        max_length = 100,
        label = "Folio de captura",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    nombreCodificador=forms.CharField(
        max_length = 100,
        label = "Nombre del codificador",
        widget = forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )

class addJurisdiccion(ModelForm):

    class Meta:
        model=Jurisdiccion
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'required': 'required'
            })
