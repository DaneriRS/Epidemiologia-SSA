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
    # folio = forms.CharField(
    #     max_length=20,
    #     label="Folio:",
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': '', 'class': 'form-control',
    #         }
    #     )
    # )
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
    # local = forms.CharField(
    #     max_length=20,
    #     label="Localidad:",
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': '', 'class': 'form-control'
    #         }
    #     )
    # )
    # entOdEL = forms.CharField(
    #     max_length=20,
    #     label="Entidad o delegacion:",
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': '', 'class': 'form-control'
    #         }
    #     )
    # )
    # cvClue = forms.CharField(
    #     max_length=20,
    #     label="Clave CLUES:",
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': '', 'class': 'form-control'
    #         }
    #     )
    # )
    # municipio1 = forms.ChoiceField(
    #     choices = MUNICIPIOS,
    #     label = 'Municipio: ',
    #     widget = forms.Select(
    #         attrs={'class': 'form-control '}
    #     )
    # )
    # institucion = forms.ChoiceField(
    #     choices = INSTITUCION,
    #     label = 'Institucion: ',
    #     widget = forms.Select(
    #         attrs={'class': 'form-control '}
    #     )
    # )
    # cvSuUni = forms.CharField(
    #     max_length=20,
    #     label="Clave suave de la unidad:",
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': '', 'class': 'form-control'
    #         }
    #     )
    # )
    # jurisdicEq = forms.ChoiceField(
    #     choices = JUROEQUI,
    #     label = 'Jurisdiccion o equivalente: ',
    #     widget = forms.Select(
    #         attrs={
    #             'class': 'form-control selectpicker',
    #             }
    #     )
    # )
    fechaNot = forms.CharField(
        label = 'Fecha de creacion',
        widget=forms.DateInput(
            format='%YYYY-%MM-%DD',
            attrs={
                'class': 'form-control', 'type': 'date',
                'data-target': '#datetimepicker1'
            }
        ),
        required=True
    )
    fechaIni = forms.CharField(
        label = 'Inicio de estudio: ',
        widget=forms.DateInput(
            format='%YYYY-%MM-%DD',
            attrs={
                'class': 'form-control', 'type': 'date',
                'data-target': '#datetimepicker1'
            }
        ),
        required=True
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
        ),
        required=True
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
    
    def __init__(self, usuario, *args, **kwargs):
        super(ContactForm1, self).__init__(*args, **kwargs)
        # Obtenemos la unidad del usuario y la asignamos como valor inicial del campo 'unidadNot'
        info = InformacionUsuario.objects.filter(user = usuario)
        self.fields['unidadNot'].initial = info.unidad
        # contactForm(usuario=2)

class ContactForm2(forms.Form):
    paciente = forms.ModelChoiceField(
        max_length=30,
        label="Num, de afiliacion o expediente: ",
        queryset=Paciente.objects.all(),
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
    fechaNot = forms.CharField(
        label = 'Fecha de Notificacion',
        widget=forms.DateInput(
            format='%YYYY-%MM-%DD',
            attrs={
                'class': 'form-control', 'type': 'date',
                'data-target': '#datetimepicker1'
            }
        )
    )
    fechaEstudio = forms.CharField(
        label = 'Inicio de estudio: ',
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

class NotificacionBrote2(forms.Form):
    DiaProHep2 = forms.ChoiceField(
        choices = TIPOHEP,
        label = 'Diagnostico probable de hepatitis: ',
        widget = forms.Select(
            attrs={
                'class': 'form-control selectpicker',
                }
        )
    )
    DiaFin2 = forms.ChoiceField(
        choices = TIPOHEP,
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
            format='%YYYY-%MM-%DD',
            attrs={
                'class': 'form-control', 'type': 'date',
                'data-target': '#datetimepicker1'
            }
        )
    )
    fechaNot3 = forms.CharField(
        label = 'Inicio de estudio: ',
        widget=forms.DateInput(
            format='%YYYY-%MM-%DD',
            attrs={
                'class': 'form-control', 'type': 'date',
                'data-target': '#datetimepicker1'
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
    manzana = forms.CharField(
        max_length=20,
        label="Manzana:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    colonia = forms.CharField(
        max_length=20,
        label="Colonia:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    localidad = forms.CharField(
        max_length=20,
        label="Localidad:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    escuela = forms.CharField(
        max_length=20,
        label="Escuela:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    guardeOvivienda = forms.CharField(
        max_length=20,
        label="Guarderia o Vivienda:",
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
    manzana = forms.CharField(
        max_length=20,
        label="Manzana:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    colonia = forms.CharField(
        max_length=20,
        label="Colonia:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    localidad = forms.CharField(
        max_length=20,
        label="Localidad:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    escuela = forms.CharField(
        max_length=20,
        label="Escuela:",
        widget=forms.TextInput(
            attrs={
                'placeholder': '', 'class': 'form-control'
            }
        )
    )
    guardeOvivienda = forms.CharField(
        max_length=20,
        label="Guarderia o Vivienda:",
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
