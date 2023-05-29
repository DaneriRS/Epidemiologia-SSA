# -*- encoding: utf-8 -*-

import os
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from datetime import date
# Create your models here.



GENEROS = (
    ('M', 'Masculino'),
    ('F', 'Femenino')
)

COLLOC = (
    ('LA', 'La aldea'),
)

MUNICIPIOS = (
    ('1', 'MORELIA'),
)

ENTIDADES = (
    ('1', 'Aguascalientes'),
    ('2', 'Baja California'),
    ('3', 'Baja California Sur'),
    ('4', 'Campeche'),
    ('5', 'Chiapas'),
    ('6', 'Chihuahua'),
    ('7', 'Coahuila'),
    ('8', 'Colima'),
    ('9', 'Distrito Federal'),
    ('10', 'Durango'),
    ('11', 'Guanajuato'),
    ('12', 'Guerrero'),
    ('13', 'Hidalgo'),
    ('14', 'Jalisco'),
    ('15', 'Michoacán'),
    ('16', 'Morelos'),
    ('17', 'Estado de México'),
    ('18', 'Nayarit'),
    ('19', 'Nuevo León'),
    ('20', 'Oaxaca'),
    ('21', 'Puebla'),
    ('22', 'Querétaro'),
    ('23', 'Quintana Roo'),
    ('24', 'San Luis Potosí'),
    ('25', 'Sinaloa'),
    ('26', 'Sonora'),
    ('27', 'Tabasco'),
    ('28', 'Tamaulipas'),
    ('29', 'Tlaxcala'),
    ('30', 'Veracruz'),
    ('31', 'Yucatán'),
    ('32', 'Zacatecas'),
)

HEPATITIS_CHOICES = (
    ('A', 'Hepatitis A'),
    ('B', 'Hepatitis B'),
    ('C', 'Hepatitis C'),
    ('D', 'Hepatitis D'),
    ('E', 'Hepatitis E'),
)

HEPATITIS_CHOICES2 = (
    ('', '--------------------'),
    ('A', 'Hepatitis A'),
    ('B', 'Hepatitis B'),
    ('C', 'Hepatitis C'),
    ('D', 'Hepatitis D'),
    ('E', 'Hepatitis E'),
)

ESCOLARIDAD_CHOICES = (
    ('NINGUNA', 'NINGUNA'),
    ('PRIMARIA INCOMPLETA', 'PRIMARIA INCOMPLETA'),
    ('SECUNDARIA INCOMPLETA', 'SECUNDARIA INCOMPLETA'),
    ('BACHILLERATO O PREPARATORIA INCOMPLETA', 'BACHILLERATO O PREPARATORIA INCOMPLETA'),
    ('PROFESIONAL', 'PROFESIONAL'),
    ('SE IGNORA', 'SE IGNORA'),
    ('PRE-ESCOLAR', 'PRE-ESCOLAR'),
    ('PRIMARIA COMPLETA', 'PRIMARIA COMPLETA'),
    ('SECUNDARIA COMPLETA', 'SECUNDARIA COMPLETA'),
    ('BACHILLERATO O PREPARATORIA COMPLETA', 'BACHILLERATO O PREPARATORIA COMPLETA'),
    ('POSGRADO', 'POSGRADO'),
)

RATIFICA_CHOICES = (
    ('Ratifica', 'Ratifica'),
    ('Rectifica', 'Rectifica'),
)

PROCEDENCIA_OPCIONES = [
    ('Local', 'Local'),
    ('Importado', 'Importado')
]
OTRA_PERSONA_OPCIONES = [
    ('Investigada', 'Investigada'),
    ('Confirmada', 'Confirmada'),
    ('Ninguna', 'Ninguna')
]
SI_NO_OPCIONES = [
    ('Si', 'Si'),
    ('No', 'No')
]
SI_NO_OPCIONES2 = [
    ('', '--------------'),
    ('Si', 'Si'),
    ('No', 'No')
]
ESTADOS_FORMULARIOS = [
    ('Tiempo1', 'Tiempo1'),
    ('Tiempo2', 'Tiempo2'),
    ('Finalizado', 'Finalizado'),
]
TIPO_ESTUDIOS_CHOICES = (
    ('PR', 'Preliminar'),
    ('CF', 'Confirmatorio'),
    ('CT', 'Control'),
)
CONTACTO_CHOICES = (
    ('I', 'Intradomiciliario'),
    ('E', 'Extradomiciliario'),
)
AFILIACION_SERVICIOS_OPCIONES = [
    ('NINGUNA', 'NINGUNA'),
    ('ISSSTE', 'ISSSTE'),
    ('SEDENA', 'SEDENA'),
    ('OTRA', 'OTRA'),
    ('SE IGNORA', 'SE IGNORA'),
    ('IMSS', 'IMSS'),
    ('PEMEX', 'PEMEX'),
    ('SEMAR', 'SEMAR'),
    ('IMSS BIENESTAR', 'IMSS BIENESTAR'),
]
CERTIFICADA_POR_OPCIONES = [
    ('MEDICO TRATANTE', 'MEDICO TRATANTE'),
    ('MEDICO LEGISTA', 'MEDICO LEGISTA'),
    ('OTRO MEDICO', 'OTRO MEDICO'),
    ('PERSONAL AUTORIZADO POR SS', 'PERSONAL AUTORIZADO POR SS'),
    ('AUTORIDAD CIVIL', 'AUTORIDAD CIVIL'),
    ('OTRO', 'OTRO'),
    ('SE IGNORA', 'SE IGNORA'),
]
class CustomUserManager(models.Manager):
    def imprimir(self):
        return self.email
    
    def is_director(self):
        return self.groups.filter(name='Director').exists()

    def is_encarJuris(self):
        return self.groups.filter(name='Encargado de Jurisdiccion').exists()
    
    def is_encarUni(self):
        return self.groups.filter(name='Encargado de unidad').exists()

    User.add_to_class('imprimir', imprimir)
    User.add_to_class('is_director', is_director)
    User.add_to_class('is_encarJuris', is_encarJuris)
    User.add_to_class('is_encarUni', is_encarUni)

class CustomUser(User):
    class Meta:
        proxy = True

    objects = CustomUserManager()

    def imprimir(cls):
        return cls.objects.imprimir()
    
    def is_director(cls):
        return cls.objects.is_director()
    
    def is_encarJuris(cls):
        return cls.objects.is_encarJuris()
    
    def is_encarUni(cls):
        return cls.objects.is_encarUni()

class Tipologia(models.Model):
    clave = models.CharField(verbose_name = "Clave", max_length = 50, unique=True)
    nombre = models.CharField(verbose_name = "Nombre", max_length = 50)
    
    def __str__(self):
        return self.clave + ' - ' + self.nombre

class Establecimiento(models.Model):
    clave = models.CharField(verbose_name = "Clave", max_length = 50, unique=True)
    nombre = models.CharField(verbose_name = "Nombre", max_length = 50)
    
    def __str__(self):
        return self.clave + ' - ' + self.nombre

class Institucion(models.Model):
    clave = models.CharField(verbose_name = "Clave", max_length = 50, unique=True)
    nombre = models.CharField(verbose_name = "Nombre", max_length = 50)
    
    def __str__(self):
        return self.clave + ' - ' + self.nombre

class Entidad(models.Model):
    clave = models.CharField(verbose_name = "Clave", max_length = 50, unique=True)
    nombre = models.CharField(verbose_name = "Nombre", max_length = 50)

    def __str__(self):
        return self.clave + ' - ' + self.nombre
    
class Jurisdiccion(models.Model):
    clave = models.CharField(verbose_name = "Clave", max_length = 50, unique=True)
    nombre = models.CharField(verbose_name = "Nombre", max_length = 50)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.clave + ' - ' + self.nombre

class Municipio(models.Model):
    clave = models.CharField(verbose_name = "Clave", max_length = 50, unique=True)
    nombre = models.CharField(verbose_name = "Nombre", max_length = 50)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.clave + ' - ' + self.nombre   

class Localidad(models.Model):
    clave = models.CharField(verbose_name = "Clave", max_length = 50)
    nombre = models.CharField(verbose_name = "Nombre", max_length = 50)
    
    
    def __str__(self):
        return self.clave + ' - ' + self.nombre

class Unidad(models.Model):
    claveclues = models.CharField(verbose_name = "Clave Clues", max_length = 50, unique=True)
    claveSuave = models.CharField(verbose_name = "Clave Suave", max_length = 50, null=True, blank=True, unique=True)
    tipologia = models.ForeignKey(Tipologia, on_delete=models.CASCADE)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    jurisdiccion = models.ForeignKey(Jurisdiccion, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.claveclues + ' - ' + str(self.jurisdiccion) + ' - ' + str(self.municipio)

class InformacionUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name = "Usuario")
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE,verbose_name = "Unidad", null=True, blank=True)
    jurisdiccion = models.ForeignKey(Jurisdiccion, on_delete=models.CASCADE,verbose_name = "Jurisdiccion")
    cargo = models.CharField(verbose_name = "Cargo", max_length=50, null=True, blank=True)

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name = "Nombre", max_length = 50)
    apellidoPa = models.CharField(verbose_name = "Apellido paterno", max_length = 50)
    apellidoMa = models.CharField(verbose_name = "Apellido materno", max_length = 50)
    numAfiliacion = models.CharField(verbose_name = "Numero de afiliacion", max_length = 50, unique = True)
    sexo = models.CharField(verbose_name = "Genero", max_length=2, choices=GENEROS)
    nacimiento = models.DateField(verbose_name = "Fecha de nacimiento")
    calle = models.CharField(verbose_name = "Calle", max_length = 50)
    numInt = models.CharField(verbose_name = "Numero interior", max_length = 50)
    numExt = models.CharField(verbose_name = "Numero exterior", max_length = 50, null=True, blank=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    codigoPostal = models.CharField(verbose_name = "Codigo postal", max_length=5)
    telefonoPaciente = models.CharField(verbose_name = "Telefono", max_length = 10)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre + ' - ' + self.apellidoPa + ' - ' + self.apellidoMa

class RegistroEstudio(models.Model):
    
    folio = models.CharField(verbose_name = "Folio", max_length=50, null=True, blank=True, unique=True)
    unidadNot = models.ForeignKey(Unidad, verbose_name="Unidad notificante", on_delete=models.SET_NULL, null=True, blank=True)
    fechaNot = models.DateField(verbose_name = "Fecha Notificacion", default=timezone.now)
    fechaIni = models.DateField(verbose_name = "Fecha Inicio Estudio")
    fechaFin = models.DateField(verbose_name = "Fecha Fin Estudio", null=True, blank=True)
    DiaProHep = models.CharField(verbose_name='Diagnóstico Probable', max_length=1, choices=HEPATITIS_CHOICES, null=True, blank=True)
    DiaFin = models.CharField(verbose_name = "Diagnóstico Final", max_length=1, choices=HEPATITIS_CHOICES, null=True, blank=True)
    otroDia = models.CharField(verbose_name = "Otro Diagnóstico", max_length=50, null=True, blank=True)
    
    paciente = models.ForeignKey(Paciente, verbose_name="Paciente", on_delete=models.SET_NULL, null=True, blank=True)
    edadAnio = models.SmallIntegerField(verbose_name="Edad (años)", null=True, blank=True)
    edadMes = models.SmallIntegerField(verbose_name="Edad (meses)", null=True, blank=True)
    edadDia = models.SmallIntegerField(verbose_name="Edad (días)", null=True, blank=True)
    
    
    
    fechaIn3 = models.DateField(verbose_name = "Fecha inicio de signos")
    signoSint3 = models.TextField(verbose_name = "Signos y sintomas")
    
    
    tratamiento3 = models.TextField(verbose_name = "Tratamiento")
    boolLab = models.BooleanField(verbose_name = "Ya se registro laboratorio", default=False)
    
    procedencia = models.CharField(verbose_name="Procedencia", max_length=10, choices=PROCEDENCIA_OPCIONES, null=True, blank=True)
    municipioProc = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True, blank=True)
    localidadProc = models.ForeignKey(Localidad, on_delete=models.SET_NULL, null=True, blank=True)
    llegadaProc = models.DateField(verbose_name = "Llegada de procedencia", null=True, blank=True)
    salidaProc = models.DateField(verbose_name = "Salida de procedencia", null=True, blank=True)
    
    otraPersona = models.CharField(verbose_name="Otra persona", max_length=20, choices=OTRA_PERSONA_OPCIONES)
    alimentos = models.CharField(verbose_name="Alimentos", max_length=20, choices=OTRA_PERSONA_OPCIONES)
    agua = models.CharField(verbose_name="Agua", max_length=20, choices=OTRA_PERSONA_OPCIONES)
    fomites = models.CharField(verbose_name="Fomites", max_length=20, choices=OTRA_PERSONA_OPCIONES)
    animales = models.CharField(verbose_name="Animales", max_length=20, choices=OTRA_PERSONA_OPCIONES)
    otrosFuentes = models.TextField(verbose_name="Otras fuentes", null=True, blank=True)
    
    personaPersona = models.CharField(verbose_name="Persona a persona", max_length=20, choices=OTRA_PERSONA_OPCIONES)
    aerea = models.CharField(verbose_name="Aerea", max_length=20, choices=OTRA_PERSONA_OPCIONES)
    digestiva = models.CharField(verbose_name="Digestiva", max_length=20, choices=OTRA_PERSONA_OPCIONES)
    fomitesMec = models.CharField(verbose_name="Fomites", max_length=20, choices=OTRA_PERSONA_OPCIONES)
    vectores = models.CharField(verbose_name="Vectores", max_length=20, choices=OTRA_PERSONA_OPCIONES)
    otrosMecanismos = models.TextField(verbose_name="Otras mecanismos", null=True, blank=True)
    
    accionesMedidas = models.TextField(verbose_name="Acciones y medidas de control")
    
    reestablecer = models.CharField(verbose_name="Se reestablecio integrante?", max_length=2, choices=SI_NO_OPCIONES, null=True, blank=True)
    secuelas = models.CharField(verbose_name="Quedo secuelas?", max_length=2, choices=SI_NO_OPCIONES, null=True, blank=True)
    portador = models.CharField(verbose_name="Quedo como portador?", max_length=2, choices=SI_NO_OPCIONES, null=True, blank=True)
    perdioCaso = models.CharField(verbose_name="Se perdio el caso?", max_length=2, choices=SI_NO_OPCIONES, null=True, blank=True)
    fallecio = models.CharField(verbose_name="Fallecio?", max_length=2, choices=SI_NO_OPCIONES, null=True, blank=True)
    fechaDefuncion = models.DateField(verbose_name = "Salida de procedencia", null=True, blank=True)
    
    platicas = models.CharField(verbose_name="Platicas de fomentos para la salud", max_length=2, choices=SI_NO_OPCIONES)
    numPlaticas = models.IntegerField(verbose_name="Numero platicas", default=0)
    vacunacion = models.CharField(verbose_name="Vacunacion", max_length=2, choices=SI_NO_OPCIONES)
    numVacunacion = models.IntegerField(verbose_name="Numero vacunacion", default=0)
    tratamientosInd = models.CharField(verbose_name="Tratamientos individuales", max_length=2, choices=SI_NO_OPCIONES)
    numTratamientosInd = models.IntegerField(verbose_name="Numero tratamientos individuales", default=0)
    tratamientosFam = models.CharField(verbose_name="Tratamientos familiares", max_length=2, choices=SI_NO_OPCIONES)
    numTratamientosFam = models.IntegerField(verbose_name="Numero tratamientos familiares", default=0)
    cloracion = models.CharField(verbose_name="Cloracion", max_length=2, choices=SI_NO_OPCIONES)
    numCloracion = models.IntegerField(verbose_name="Numero cloracion", default=0)
    letrinizacion = models.CharField(verbose_name="Letrinizacion", max_length=2, choices=SI_NO_OPCIONES)
    numLetrinizacion = models.IntegerField(verbose_name="Numero letrinizacion", default=0)
    otrasActividades = models.TextField(verbose_name="Otras actividades")
    
    comentariosConclusiones = models.TextField(verbose_name="Comentarios y conclusion")
    
    
    fechaCap = models.DateField(verbose_name = "Fecha Captura", default=timezone.now)
    capturante = models.ForeignKey(User, verbose_name="Capturante", on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.CharField(verbose_name="Estado del formulario", max_length=30, choices=ESTADOS_FORMULARIOS)
    
    def save(self, *args, **kwargs):
        if self.edadAnio is None or self.edadMes is None or self.edadDia is None:
            # Calcula la edad en base a la fecha de nacimiento y la fecha actual
            if self.paciente and self.paciente.nacimiento:
                fecha_actual = date.today()
                fecha_nacimiento = self.paciente.nacimiento

                edad = fecha_actual - fecha_nacimiento

                # Calcula la edad en años, meses y días
                edad_anio = edad.days // 365
                edad_mes = (edad.days % 365) // 30
                edad_dia = (edad.days % 365) % 30

                # Actualiza los campos de edad si están vacíos o son None
                if self.edadAnio is None or self.edadAnio == '':
                    self.edadAnio = edad_anio

                if self.edadMes is None or self.edadMes == '':
                    self.edadMes = edad_mes

                if self.edadDia is None or self.edadDia == '':
                    self.edadDia = edad_dia

        super(RegistroEstudio, self).save(*args, **kwargs)
    
class Estudio(models.Model):
    nombre = models.CharField(verbose_name = "Nombre de estudio", max_length=100)
    tipo = models.CharField(verbose_name = "Tipo", choices=TIPO_ESTUDIOS_CHOICES, max_length=2)
    fecha = models.DateField(verbose_name = "Fecha")
    resultado = models.CharField(verbose_name = "Resultado", max_length=100)
    registroEstudio = models.ForeignKey(RegistroEstudio, on_delete=models.CASCADE)
    
class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name = "Nombre", max_length=100)
    domicilio = models.CharField(verbose_name = "Domicilio", max_length=100)
    edad = models.SmallIntegerField(verbose_name = "Edad")
    sexo = models.CharField(verbose_name = "Sexo", max_length=10, choices=GENEROS)
    contacto = models.CharField(verbose_name = "Sexo", max_length=20, choices=CONTACTO_CHOICES)
    caso = models.CharField(verbose_name = "Caso", max_length=2, choices=SI_NO_OPCIONES)
    registroEstudio = models.ForeignKey(RegistroEstudio, on_delete=models.CASCADE)

    
class Logos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=250, blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True, verbose_name="Imagen")
    actualizado = models.DateTimeField('Fecha de actualización', auto_now_add=True)

    def save(self, *args, **kwargs):
        img = Image.open(self.logo.path)

        if img.height > 82:
            output_size = (300,80)
            img.thumbnail(output_size, Image.LANCZOS)
            img.save(self.logo.path)
        
        super().save(*args, **kwargs)

class NotificacionBrote(models.Model):
    folio = models.CharField(verbose_name = "Folio", max_length=50, null=True, blank=True, unique=True)
    unidadNot = models.ForeignKey(Unidad, verbose_name="Unidad notificante", on_delete=models.SET_NULL, null=True, blank=True)
    fechaNot = models.DateField(verbose_name = "Fecha Notificacion", default=timezone.now)
    fechaInicio = models.DateField(verbose_name = "Fecha Inicio Estudio", default=timezone.now)
    fechaTerminacion = models.DateField(verbose_name = "Fecha Terminacion Estudio", null=True, blank=True)
    diaProHep = models.CharField(verbose_name='Diagnóstico Probable', max_length=1, choices=HEPATITIS_CHOICES)
    diaFin = models.CharField(verbose_name = "Diagnóstico Final", max_length=1, choices=HEPATITIS_CHOICES, null=True, blank=True)
    otroDiag = models.CharField(verbose_name = "Otro diagnostico", max_length=100, null=True, blank=True)

    DiaProHep2 = models.CharField(verbose_name='Diagnóstico Probable', max_length=1, choices=HEPATITIS_CHOICES)
    DiaFin2 = models.CharField(verbose_name = "Diagnóstico Final", max_length=1, choices=HEPATITIS_CHOICES, null=True, blank=True)
    fechaNot2 = models.DateField(verbose_name = "Fecha Notificacion", default=timezone.now)
    fechaNot3 = models.DateField(verbose_name = "Fecha Notificacion", default=timezone.now)
    casosProbables = models.SmallIntegerField(verbose_name = "Casos probables")
    casosConfirmados = models.SmallIntegerField(verbose_name = "Casos confirmados")
    hospitalizados = models.SmallIntegerField(verbose_name = "Hospitalizados")
    defunciones = models.SmallIntegerField(verbose_name="Defunciones")

    anteEpiBrote = models.TextField(verbose_name = "Antecedentes epidemiologicos del brote")
    probFuenBrote = models.TextField(verbose_name = "Probables fuentes del brote")
    probMecTransmision = models.TextField(verbose_name = "Probables mecanismos de transmision")

    accionesPrevControl = models.TextField(verbose_name = "Acciones de prevencion y control realizadas (Anotar fecha de inicio)")
    
    capturante = models.ForeignKey(User, verbose_name="Capturante", on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.CharField(verbose_name="Estado del formulario", max_length=30, choices=ESTADOS_FORMULARIOS)
    
class NumerosCasos(models.Model):
    menor1MascNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos menores a 1 anio masculinos", default=0)
    menor1FemNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos menores a 1 anio femeninos", default=0)
    menor1TotNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos menores a 1 anio totales", default=0)
    
    de14MascNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 1 a 4 anios masculinos", default=0)
    de14FemNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 1 a 4 anios femeninos", default=0)
    de14TotNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 1 a 4 anios totales", default=0)
    
    de59MascNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 5 a 9 anios masculinos", default=0)
    de59FemNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 5 a 9 anios femeninos", default=0)
    de59TotNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 5 a 9 anios totales", default=0)
    
    de1014MascNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 10 a 14 anios masculinos", default=0)
    de1014FemNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 10 a 14 anios femeninos", default=0)
    de1014TotNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 10 a 14 anios totales", default=0)
    
    de1519MascNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 15 a 19 anio masculinos", default=0)
    de1519FemNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 15 a 19 anio femeninos", default=0)
    de1519TotNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 15 a 19 anio totales", default=0)
    
    de2024MascNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 20 a 24 anios masculinos", default=0)
    de2024FemNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 20 a 24 anios femeninos", default=0)
    de2024TotNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 20 a 24 anios totales", default=0)
    
    de2544MascNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 25 a 44 anios masculinos", default=0)
    de2544FemNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 25 a 44 anios femeninos", default=0)
    de2544TotNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 25 a 44 anios totales", default=0)
    
    de4549MascNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 45 a 49 anios masculinos", default=0)
    de4549FemNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 45 a 49 anios femeninos", default=0)
    de4549TotNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 45 a 49 anios totales", default=0)
    
    de5059MascNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 50 a 59 anios masculinos", default=0)
    de5059FemNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 50 a 59 anios femeninos", default=0)
    de5059TotNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 50 a 59 anios totales", default=0)
    
    de6064MascNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 60 a 64 anios masculinos", default=0)
    de6064FemNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 60 a 64 anios femeninos", default=0)
    de6064TotNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de 60 a 64 anios totales", default=0)
    
    mas65MascNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de mayores a 65 anios masculinos", default=0)
    mas65FemNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de mayores a 65 anios femeninos", default=0)
    mas65TotNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos de mayores a 65 anios totales", default=0)
    
    seIgnoraMascNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos donde se ignora la edad en masculinos", default=0)
    seIgnoraFemNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos donde se ignora la edad en femeninos", default=0)
    seIgnoraTotNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos donde se ignora la edad en totales", default=0)
    
    totalMascNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos totales masculinos", default=0)
    totalFemNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos totales femeninos", default=0)
    totalTotNumerosCasos = models.SmallIntegerField(verbose_name="Numero de casos totales", default=0)
    
    notifBroteNumerosCasos = models.ForeignKey(NotificacionBrote, on_delete=models.CASCADE)
    
class NumerosDefunciones(models.Model):
    menor1MascNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones menores a 1 anio masculinos", default=0)
    menor1FemNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones menores a 1 anio femeninos", default=0)
    menor1TotNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones menores a 1 anio totales", default=0)
    
    de14MascNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 1 a 4 anios masculinos", default=0)
    de14FemNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 1 a 4 anios femeninos", default=0)
    de14TotNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 1 a 4 anios totales", default=0)
    
    de59MascNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 5 a 9 anios masculinos", default=0)
    de59FemNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 5 a 9 anios femeninos", default=0)
    de59TotNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 5 a 9 anios totales", default=0)
    
    de1014MascNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 10 a 14 anios masculinos", default=0)
    de1014FemNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 10 a 14 anios femeninos", default=0)
    de1014TotNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 10 a 14 anios totales", default=0)
    
    de1519MascNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 15 a 19 anio masculinos", default=0)
    de1519FemNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 15 a 19 anio femeninos", default=0)
    de1519TotNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 15 a 19 anio totales", default=0)
    
    de2024MascNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 20 a 24 anios masculinos", default=0)
    de2024FemNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 20 a 24 anios femeninos", default=0)
    de2024TotNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 20 a 24 anios totales", default=0)
    
    de2544MascNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 25 a 44 anios masculinos", default=0)
    de2544FemNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 25 a 44 anios femeninos", default=0)
    de2544TotNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 25 a 44 anios totales", default=0)
    
    de4549MascNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 45 a 49 anios masculinos", default=0)
    de4549FemNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 45 a 49 anios femeninos", default=0)
    de4549TotNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 45 a 49 anios totales", default=0)
    
    de5059MascNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 50 a 59 anios masculinos", default=0)
    de5059FemNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 50 a 59 anios femeninos", default=0)
    de5059TotNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 50 a 59 anios totales", default=0)
    
    de6064MascNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 60 a 64 anios masculinos", default=0)
    de6064FemNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 60 a 64 anios femeninos", default=0)
    de6064TotNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de 60 a 64 anios totales", default=0)
    
    mas65MascNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de mayores a 65 anios masculinos", default=0)
    mas65FemNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de mayores a 65 anios femeninos", default=0)
    mas65TotNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones de mayores a 65 anios totales", default=0)
    
    seIgnoraMascNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones donde se ignora la edad en masculinos", default=0)
    seIgnoraFemNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones donde se ignora la edad en femeninos", default=0)
    seIgnoraTotNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones donde se ignora la edad en totales", default=0)
    
    totalMascNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones totales masculinos", default=0)
    totalFemNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones totales femeninos", default=0)
    totalTotNumerosDefunciones = models.SmallIntegerField(verbose_name="Numero de defunciones totales", default=0)
    
    notifBroteNumerosDefunciones = models.ForeignKey(NotificacionBrote, on_delete=models.CASCADE)
    
class PoblacionExpuesta(models.Model):
    menor1MascPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta menores a 1 anio masculinos", default=0)
    menor1FemPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta menores a 1 anio femeninos", default=0)
    menor1TotPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta menores a 1 anio totales", default=0)
    
    de14MascPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 1 a 4 anios masculinos", default=0)
    de14FemPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 1 a 4 anios femeninos", default=0)
    de14TotPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 1 a 4 anios totales", default=0)
    
    de59MascPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 5 a 9 anios masculinos", default=0)
    de59FemPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 5 a 9 anios femeninos", default=0)
    de59TotPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 5 a 9 anios totales", default=0)
    
    de1014MascPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 10 a 14 anios masculinos", default=0)
    de1014FemPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 10 a 14 anios femeninos", default=0)
    de1014TotPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 10 a 14 anios totales", default=0)
    
    de1519MascPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 15 a 19 anio masculinos", default=0)
    de1519FemPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 15 a 19 anio femeninos", default=0)
    de1519TotPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 15 a 19 anio totales", default=0)
    
    de2024MascPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 20 a 24 anios masculinos", default=0)
    de2024FemPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 20 a 24 anios femeninos", default=0)
    de2024TotPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 20 a 24 anios totales", default=0)
    
    de2544MascPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 25 a 44 anios masculinos", default=0)
    de2544FemPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 25 a 44 anios femeninos", default=0)
    de2544TotPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 25 a 44 anios totales", default=0)
    
    de4549MascPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 45 a 49 anios masculinos", default=0)
    de4549FemPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 45 a 49 anios femeninos", default=0)
    de4549TotPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 45 a 49 anios totales", default=0)
    
    de5059MascPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 50 a 59 anios masculinos", default=0)
    de5059FemPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 50 a 59 anios femeninos", default=0)
    de5059TotPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 50 a 59 anios totales", default=0)
    
    de6064MascPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 60 a 64 anios masculinos", default=0)
    de6064FemPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 60 a 64 anios femeninos", default=0)
    de6064TotPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de 60 a 64 anios totales", default=0)
    
    mas65MascPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de mayores a 65 anios masculinos", default=0)
    mas65FemPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de mayores a 65 anios femeninos", default=0)
    mas65TotPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta de mayores a 65 anios totales", default=0)
    
    seIgnoraMascPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta donde se ignora la edad en masculinos", default=0)
    seIgnoraFemPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta donde se ignora la edad en femeninos", default=0)
    seIgnoraTotPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta donde se ignora la edad en totales", default=0)
    
    totalMascPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta totales masculinos", default=0)
    totalFemPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta totales femeninos", default=0)
    totalTotPoblacionExpuesta = models.SmallIntegerField(verbose_name="Poblacion expuesta totales", default=0)
    
    notifBrotePoblacionExpuesta = models.ForeignKey(NotificacionBrote, on_delete=models.CASCADE)
    
class TasaAtaque(models.Model):
    menor1MascTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque menores a 1 anio masculinos", default=0)
    menor1FemTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque menores a 1 anio femeninos", default=0)
    menor1TotTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque menores a 1 anio totales", default=0)
    
    de14MascTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 1 a 4 anios masculinos", default=0)
    de14FemTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 1 a 4 anios femeninos", default=0)
    de14TotTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 1 a 4 anios totales", default=0)
    
    de59MascTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 5 a 9 anios masculinos", default=0)
    de59FemTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 5 a 9 anios femeninos", default=0)
    de59TotTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 5 a 9 anios totales", default=0)
    
    de1014MascTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 10 a 14 anios masculinos", default=0)
    de1014FemTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 10 a 14 anios femeninos", default=0)
    de1014TotTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 10 a 14 anios totales", default=0)
    
    de1519MascTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 15 a 19 anio masculinos", default=0)
    de1519FemTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 15 a 19 anio femeninos", default=0)
    de1519TotTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 15 a 19 anio totales", default=0)
    
    de2024MascTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 20 a 24 anios masculinos", default=0)
    de2024FemTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 20 a 24 anios femeninos", default=0)
    de2024TotTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 20 a 24 anios totales", default=0)
    
    de2544MascTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 25 a 44 anios masculinos", default=0)
    de2544FemTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 25 a 44 anios femeninos", default=0)
    de2544TotTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 25 a 44 anios totales", default=0)
    
    de4549MascTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 45 a 49 anios masculinos", default=0)
    de4549FemTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 45 a 49 anios femeninos", default=0)
    de4549TotTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 45 a 49 anios totales", default=0)
    
    de5059MascTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 50 a 59 anios masculinos", default=0)
    de5059FemTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 50 a 59 anios femeninos", default=0)
    de5059TotTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 50 a 59 anios totales", default=0)
    
    de6064MascTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 60 a 64 anios masculinos", default=0)
    de6064FemTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 60 a 64 anios femeninos", default=0)
    de6064TotTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de 60 a 64 anios totales", default=0)
    
    mas65MascTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de mayores a 65 anios masculinos", default=0)
    mas65FemTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de mayores a 65 anios femeninos", default=0)
    mas65TotTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque de mayores a 65 anios totales", default=0)
    
    seIgnoraMascTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque donde se ignora la edad en masculinos", default=0)
    seIgnoraFemTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque donde se ignora la edad en femeninos", default=0)
    seIgnoraTotTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque donde se ignora la edad en totales", default=0)
    
    totalMascTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque totales masculinos", default=0)
    totalFemTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque totales femeninos", default=0)
    totalTotTasaAtaque = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de ataque totales", default=0)
    
    notifBroteTasaAtaque = models.ForeignKey(NotificacionBrote, on_delete=models.CASCADE)
    
class TasaLetalidad(models.Model):
    menor1MascTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad menores a 1 anio masculinos", default=0)
    menor1FemTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad menores a 1 anio femeninos", default=0)
    menor1TotTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad menores a 1 anio totales", default=0)
    
    de14MascTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 1 a 4 anios masculinos", default=0)
    de14FemTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 1 a 4 anios femeninos", default=0)
    de14TotTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 1 a 4 anios totales", default=0)
    
    de59MascTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 5 a 9 anios masculinos", default=0)
    de59FemTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 5 a 9 anios femeninos", default=0)
    de59TotTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 5 a 9 anios totales", default=0)
    
    de1014MascTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 10 a 14 anios masculinos", default=0)
    de1014FemTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 10 a 14 anios femeninos", default=0)
    de1014TotTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 10 a 14 anios totales", default=0)
    
    de1519MascTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 15 a 19 anio masculinos", default=0)
    de1519FemTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 15 a 19 anio femeninos", default=0)
    de1519TotTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 15 a 19 anio totales", default=0)
    
    de2024MascTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 20 a 24 anios masculinos", default=0)
    de2024FemTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 20 a 24 anios femeninos", default=0)
    de2024TotTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 20 a 24 anios totales", default=0)
    
    de2544MascTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 25 a 44 anios masculinos", default=0)
    de2544FemTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 25 a 44 anios femeninos", default=0)
    de2544TotTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 25 a 44 anios totales", default=0)
    
    de4549MascTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 45 a 49 anios masculinos", default=0)
    de4549FemTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 45 a 49 anios femeninos", default=0)
    de4549TotTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 45 a 49 anios totales", default=0)
    
    de5059MascTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 50 a 59 anios masculinos", default=0)
    de5059FemTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 50 a 59 anios femeninos", default=0)
    de5059TotTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 50 a 59 anios totales", default=0)
    
    de6064MascTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 60 a 64 anios masculinos", default=0)
    de6064FemTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 60 a 64 anios femeninos", default=0)
    de6064TotTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de 60 a 64 anios totales", default=0)
    
    mas65MascTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de mayores a 65 anios masculinos", default=0)
    mas65FemTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de mayores a 65 anios femeninos", default=0)
    mas65TotTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad de mayores a 65 anios totales", default=0)
    
    seIgnoraMascTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad donde se ignora la edad en masculinos", default=0)
    seIgnoraFemTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad donde se ignora la edad en femeninos", default=0)
    seIgnoraTotTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad donde se ignora la edad en totales", default=0)
    
    totalMascTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad totales masculinos", default=0)
    totalFemTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad totales femeninos", default=0)
    totalTotTasaLetalidad = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Tasa de letalidad totales", default=0)
    
    notifBroteTasaLetalidad = models.ForeignKey(NotificacionBrote, on_delete=models.CASCADE)
    
class SignosSintomas(models.Model):
    menor1SignosSignosSintomas = models.TextField(verbose_name="Signos y sintomas menores a 1 anio", null=True, blank=True)
    menor1NumSignosSintomas = models.SmallIntegerField(verbose_name="Casos menores a 1 anio", default=0)
    menor1PorcSignosSintomas = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Porcentaje 1 anio", default=0)
    
    de14SignosSignosSintomas = models.TextField(verbose_name="Signos y sintomas de 1 a 4 anios", null=True, blank=True)
    de14NumSignosSintomas = models.SmallIntegerField(verbose_name="Casos de 1 a 4 anios", default=0)
    de14PorcSignosSintomas = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Porcentaje de 1 a 4 anios", default=0)
    
    de59SignosSignosSintomas = models.TextField(verbose_name="Signos y sintomas de 5 a 9 anios", null=True, blank=True)
    de59NumSignosSintomas = models.SmallIntegerField(verbose_name="Casos de 5 a 9 anios", default=0)
    de59PorcSignosSintomas = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Porcentaje de 5 a 9 anios", default=0)
    
    de1014SignosSignosSintomas = models.TextField(verbose_name="Signos y sintomas de 10 a 14 anios", null=True, blank=True)
    de1014NumSignosSintomas = models.SmallIntegerField(verbose_name="Casos de 10 a 14 anios", default=0)
    de1014PorcSignosSintomas = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Porcentaje de 10 a 14 anios", default=0)
    
    de1519SignosSignosSintomas = models.TextField(verbose_name="Signos y sintomas de 15 a 19 anio", null=True, blank=True)
    de1519NumSignosSintomas = models.SmallIntegerField(verbose_name="Casos de 15 a 19 anio", default=0)
    de1519PorcSignosSintomas = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Porcentaje de 15 a 19 anio", default=0)
    
    de2024SignosSignosSintomas = models.TextField(verbose_name="Signos y sintomas de 20 a 24 anios", null=True, blank=True)
    de2024NumSignosSintomas = models.SmallIntegerField(verbose_name="Casos de 20 a 24 anios", default=0)
    de2024PorcSignosSintomas = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Porcentaje de 20 a 24 anios", default=0)
    
    de2544SignosSignosSintomas = models.TextField(verbose_name="Signos y sintomas de 25 a 44 anios", null=True, blank=True)
    de2544NumSignosSintomas = models.SmallIntegerField(verbose_name="Casos de 25 a 44 anios", default=0)
    de2544PorcSignosSintomas = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Porcentaje de 25 a 44 anios", default=0)
    
    de4549SignosSignosSintomas = models.TextField(verbose_name="Signos y sintomas de 45 a 49 anios", null=True, blank=True)
    de4549NumSignosSintomas = models.SmallIntegerField(verbose_name="Casos de 45 a 49 anios", default=0)
    de4549PorcSignosSintomas = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Porcentaje de 45 a 49 anios", default=0)
    
    de5059SignosSignosSintomas = models.TextField(verbose_name="Signos y sintomas de 50 a 59 anios", null=True, blank=True)
    de5059NumSignosSintomas = models.SmallIntegerField(verbose_name="Casos de 50 a 59 anios", default=0)
    de5059PorcSignosSintomas = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Porcentaje de 50 a 59 anios", default=0)
    
    de6064SignosSignosSintomas = models.TextField(verbose_name="Signos y sintomas de 60 a 64 anios", null=True, blank=True)
    de6064NumSignosSintomas = models.SmallIntegerField(verbose_name="Casos de 60 a 64 anios", default=0)
    de6064PorcSignosSintomas = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Porcentaje de 60 a 64 anios", default=0)
    
    mas65SignosSignosSintomas = models.TextField(verbose_name="Signos y sintomas de mayores a 65 anios", null=True, blank=True)
    mas65NumSignosSintomas = models.SmallIntegerField(verbose_name="Casos de mayores a 65 anios", default=0)
    mas65PorcSignosSintomas = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Porcentaje de mayores a 65 anios", default=0)
    
    seIgnoraSignosSignosSintomas = models.TextField(verbose_name="Signos y sintomas donde se ignora la edad en", null=True, blank=True)
    seIgnoraNumSignosSintomas = models.SmallIntegerField(verbose_name="Casos donde se ignora la edad en", default=0)
    seIgnoraPorcSignosSintomas = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Porcentaje donde se ignora la edad en", default=0)
    
    totalSignosSignosSintomas = models.TextField(verbose_name="Signos y sintomas totales", null=True, blank=True)
    totalNumSignosSintomas = models.SmallIntegerField(verbose_name="Casos totales", default=0)
    totalPorcSignosSintomas = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Porcentaje totales", default=100)
    
    notifBroteSignosSintomas = models.ForeignKey(NotificacionBrote, on_delete=models.CASCADE)
    
class PuntoGrafico(models.Model):
    numeroCasosPuntoGrafico = models.SmallIntegerField(verbose_name="Numero de casos en un punto temporal", default=0)
    puntoTemporal = models.SmallIntegerField(verbose_name="Punto temporal", default=0)
    clave = models.CharField(verbose_name="clave", max_length=100)
    notifBrote = models.ForeignKey(NotificacionBrote, on_delete=models.CASCADE)

class DistribucionGeografica(models.Model):
    area = models.CharField(verbose_name = "Área, Manzana, Colonia, Localidad, Escuela, Guardería O Vivienda", max_length=100)
    numeroCasosDistribucionGeografica = models.SmallIntegerField(verbose_name = "Numero de casos", default=0)
    numeroCasosPorc = models.DecimalField(max_digits=8, decimal_places=5, verbose_name = "Porcentaje de casos", default=0)
    numeroDefunciones = models.SmallIntegerField(verbose_name = "Numero de defunciones", default=0)
    numeroDefuncionesPorc = models.DecimalField(max_digits=8, decimal_places=5, verbose_name = "Porcentaje de defunciones", default=0)
    croquis = models.CharField(verbose_name="Enlace del croquis", max_length=1000, null=True, blank=True)
    notificacionBrote = models.ForeignKey(NotificacionBrote, on_delete=models.CASCADE)

class Anexo8(models.Model):
    nombreFallecido = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    edadAnio = models.SmallIntegerField(verbose_name="Edad en Anio")
    edadMes = models.SmallIntegerField(verbose_name="Edad en Mes")
    edadDia = models.SmallIntegerField(verbose_name="Edad en Dia")
    edadHora = models.SmallIntegerField(verbose_name="Edad en Hora", null=True, blank=True)
    edadMin = models.SmallIntegerField(verbose_name="Edad en Minuto", null=True, blank=True)
    # institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE) Trata de lo mismo pero se manejan otras opciones de acuerdo al INEGI 
    afiliacionServicios = models.CharField(verbose_name="Afiliacion de Servicios Medicos", max_length=20, choices=AFILIACION_SERVICIOS_OPCIONES)
    fechaDefuncion = models.DateField(verbose_name = "Fecha de defunción", null=True, blank=True)
    escolaridad = models.CharField(verbose_name='Escolaridad', max_length=50, choices=ESCOLARIDAD_CHOICES)
    ocupacion = models.CharField(verbose_name='Ocupación', max_length=50)
    certificadaPor = models.CharField(verbose_name='Certificada por', max_length=50, choices=CERTIFICADA_POR_OPCIONES)
    lugardeResidenciaMuni = models.ForeignKey(Municipio, on_delete=models.CASCADE, verbose_name="Lugar de residencia habitual, Municipio")
    lugardeResidenciaEnti = models.ForeignKey(Entidad, on_delete=models.CASCADE, verbose_name="Lugar de residencia habitual, Entidad")
    lugarDefMuni = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='municipioDef', verbose_name="Lugar donde ocurrio la defuncion, Municipio")
    lugarDefEnti = models.ForeignKey(Entidad, on_delete=models.CASCADE, related_name='entidadDef', verbose_name="Lugar donde ocurrio la defuncion, Entidad")
    nombreCertificante = models.CharField(verbose_name="Nombre del Certificante", max_length=30)

    causasDefI = models.CharField(verbose_name="Causas de defunción I (1)", max_length=100)
    causaDefInterI = models.CharField(verbose_name="Causas de defunción I (1) Intervalo", max_length=100)
    causaDefCodigoCieI = models.CharField(verbose_name="Causas de defunción I (1) Codigo CIE", max_length=4)
    causaBasicaI = models.CharField(verbose_name="Causas de defunción I (1) Causa Basica", max_length=100)
    causasDefI2 = models.CharField(verbose_name="Causas de defunción I (2)", max_length=100)
    causaDefInterI2 = models.CharField(verbose_name="Causas de defunción I (2) Intervalo", max_length=100)
    causaDefCodigoCieI2 = models.CharField(verbose_name="Causas de defunción I (2) Codigo CIE", max_length=4)
    causasDefI3 = models.CharField(verbose_name="Causas de defunción I (3)", max_length=100)
    causaDefInterI3 = models.CharField(verbose_name="Causas de defunción I (3) Intervalo", max_length=100)
    causaDefCodigoCieI3 = models.CharField(verbose_name="Causas de defunción I (3) Codigo CIE", max_length=4)
    causasDefI4 = models.CharField(verbose_name="Causas de defunción I (4)", max_length=100)
    causaDefInterI4 = models.CharField(verbose_name="Causas de defunción I (4) Intervalo", max_length=100)
    causaDefCodigoCieI4 = models.CharField(verbose_name="Causas de defunción I (4) Codigo CIE", max_length=4)
    causasDefII1 = models.CharField(verbose_name="Causas de defunción II (1)", max_length=100)
    causaDefInterII1 = models.CharField(verbose_name="Causas de defunción II (1) Intervalo", max_length=100)
    causaDefCodigoCieII1 = models.CharField(verbose_name="Causas de defunción II (1) Codigo CIE", max_length=4)
    causasDefII2 = models.CharField(verbose_name="Causas de defunción II (2)", max_length=100)
    causaDefInterII2 = models.CharField(verbose_name="Causas de defunción II (2) Intervalo", max_length=100)
    causaDefCodigoCieII2 = models.CharField(verbose_name="Causas de defunción II (2) Codigo CIE", max_length=4)
    causaVigEpi = models.CharField(verbose_name="Causa sujeta a vigilancia epidemiologica", max_length=100)
    causaVigEpiCodigoCie = models.CharField(verbose_name="Causa sujeta a vigilancia epidemiologica, Codigo CIE", max_length=4)

    causaVigEpi2 = models.CharField(verbose_name="Causa sujeta a vigilancia epidemiologica 2", max_length=100, blank=True, null=True)
    ratifica = models.CharField(verbose_name="Ratifica", max_length=20, choices=RATIFICA_CHOICES)
    causasDef2I = models.CharField(verbose_name="Causas de defunción 2 I (1)", max_length=100, blank=True, null=True)
    causaDefInter2I = models.CharField(verbose_name="Causas de defunción 2 I (1) Intervalo", max_length=100, blank=True, null=True)
    causaDefCodigoCi22I = models.CharField(verbose_name="Causas de defunción 2 I (1) Codigo CIE", max_length=4, blank=True, null=True)
    causaBasica2I = models.CharField(verbose_name="Causas de defunción 2 I (1) Causa Basica", max_length=100, blank=True, null=True)
    causasDef2I2 = models.CharField(verbose_name="Causas de defunción 2 I (2)", max_length=100, blank=True, null=True)
    causaDefInter2I2 = models.CharField(verbose_name="Causas de defunción 2 I (2) Intervalo", max_length=100, blank=True, null=True)
    causaDefCodigoCie2I2 = models.CharField(verbose_name="Causas de defunción 2 I (2) Codigo CIE", max_length=4, blank=True, null=True)
    causasDef2I3 = models.CharField(verbose_name="Causas de defunción 2 I (3)", max_length=100, blank=True, null=True)
    causaDefInter2I3 = models.CharField(verbose_name="Causas de defunción 2 I (3) Intervalo", max_length=100, blank=True, null=True)
    causaDefCodigoCie2I3 = models.CharField(verbose_name="Causas de defunción 2 I (3) Codigo CIE", max_length=4, blank=True, null=True)
    causasDef2I4 = models.CharField(verbose_name="Causas de defunción 2 I (4)", max_length=100, blank=True, null=True)
    causaDefInter2I4 = models.CharField(verbose_name="Causas de defunción 2 I (4) Intervalo", max_length=100, blank=True, null=True)
    causaDefCodigoCie2I4 = models.CharField(verbose_name="Causas de defunción 2 I (4) Codigo CIE", max_length=4, blank=True, null=True)
    causasDef2II1 = models.CharField(verbose_name="Causas de defunción 2 II (1)", max_length=100, blank=True, null=True)
    causaDefInter2II1 = models.CharField(verbose_name="Causas de defunción 2 II (1) Intervalo", max_length=100, blank=True, null=True)
    causaDefCodigoCie2II1 = models.CharField(verbose_name="Causas de defunción 2 II (1) Codigo CIE", max_length=4, blank=True, null=True)
    causasDef2II2 = models.CharField(verbose_name="Causas de defunción 2 II (2)", max_length=100, blank=True, null=True)
    causaDefInter2II2 = models.CharField(verbose_name="Causas de defunción 2 II (2) Intervalo", max_length=100, blank=True, null=True)
    causaDefCodigoCie2II2 = models.CharField(verbose_name="Causas de defunción 2 II (2) Codigo CIE", max_length=4, blank=True, null=True)
    
    # causaVigEpiCodigoCie2 = models.CharField(verbose_name="Causa sujeta a vigilancia epidemiologica 2, Codigo CIE", max_length=4, blank=True, null=True)
    # causaVigEpi2 = models.CharField(verbose_name="Causa sujeta a vigilancia epidemiologica", max_length=100)
    # causasDef3 = models.CharField(verbose_name="Causas de defunción3", max_length=200)
    # causasDef4 = models.CharField(verbose_name="Causas de defunción4", max_length=100)
    fechaRecoleccion = models.DateField(verbose_name = "Fecha de recolección", null=True, blank=True)
    fechaInicio = models.DateField(verbose_name = "Fecha de inicio", null=True, blank=True)
    fechaConclusion = models.DateField(verbose_name = "Fecha de conclusión", null=True, blank=True)
    reporteInegi = models.DateField(verbose_name = "Fecha de reporte a INEGI", null=True, blank=True)
    observaciones = models.TextField(verbose_name="Observaciones")
    nombreResponsableInv = models.CharField(verbose_name="Nombre del responsable de la investigación", max_length=50)
    apellidoPaResponsableInv = models.CharField(verbose_name="Apellido paterno del responsable de la investigación", max_length=50)
    apellidoMaResponsableInv = models.CharField(verbose_name="Apellido materno del responsable de la investigación", max_length=50)
    cargo = models.CharField(verbose_name="Cargo", max_length=50, null=True, blank=True)
    firma = models.CharField(verbose_name="Firma", max_length=50, null=True, blank=True)

    tipoDocumento = models.CharField(verbose_name="Tipo de documento", max_length=50, null=True, blank=True)
    numPaquete = models.CharField(verbose_name="Número de paquete", max_length=50, null=True, blank=True)
    numActa = models.CharField(verbose_name="Número de acta", max_length=50, null=True, blank=True)
    folioCaptura = models.CharField(verbose_name="Folio de captura", max_length=50, null=True, blank=True)
    nombreCodificador = models.CharField(verbose_name="Nombre del codificador", max_length=50, null=True, blank=True)
    
    capturante = models.ForeignKey(User, verbose_name="Capturante", on_delete=models.SET_NULL, null=True, blank=True)
    