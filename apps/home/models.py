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
    ('F', 'Femenino'),
    ('NB', 'No Binario'),
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

ESCOLARIDAD_CHOICES = (
    ('1', 'Ninguna'),
    ('2', 'Preescolar'),
    ('3', 'Primaria Incompleta'),
    ('4', 'Primaria Completa'),
    ('5', 'Secundaria Incompleta'),
    ('6', 'Secundaria Completa'),
    ('7', 'Preparatoria Incompleta'),
    ('8', 'Preparatoria Completa'),
    ('9', 'Profesional'),
    ('10', 'Posgrado'),
    ('11', 'Se ignora'),

)

RATIFICA_CHOICES = (
    ('1', 'Ratifica'),
    ('2', 'Rectifica'),
)
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
        return self.claveclues

class InformacionUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name = "Usuario")
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE,verbose_name = "Unidad", null=True, blank=True)
    jurisdiccion = models.ForeignKey(Jurisdiccion, on_delete=models.CASCADE,verbose_name = "Jurisdiccion")

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
    numExt = models.CharField(verbose_name = "Numero exterior", max_length = 50)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    codigoPostal = models.CharField(verbose_name = "Codigo postal", max_length=5)
    telefonoPaciente = models.CharField(verbose_name = "Telefono", max_length = 10)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre + ' - ' + self.apellidoPa + ' - ' + self.apellidoMa

class RegistroEstudio(models.Model):
    PROCEDENCIA_OPCIONES = [
        ('local', 'Local'),
        ('importado', 'Importado')
    ]
    OTRA_PERSONA_OPCIONES = [
        ('investigada', 'Investigada'),
        ('confirmada', 'Confirmada'),
        ('ninguna', 'Ninguna')
    ]
    folio = models.CharField(verbose_name = "Folio", max_length=50, null=True, blank=True, unique=True)
    unidadNot = models.ForeignKey(Unidad, verbose_name="Unidad notificante", on_delete=models.SET_NULL, null=True, blank=True)
    fechaNot = models.DateField(verbose_name = "Fecha Notificacion", default=timezone.now)
    fechaIni = models.DateField(verbose_name = "Fecha Inicio Estudio")
    fechaFin = models.DateField(verbose_name = "Fecha Fin Estudio", null=True, blank=True)
    DiaProHep = models.CharField(verbose_name='Diagnóstico Probable', max_length=1, choices=HEPATITIS_CHOICES, null=True, blank=True)
    DiaFin = models.CharField(verbose_name = "Diagnóstico Final", max_length=1, choices=HEPATITIS_CHOICES, null=True, blank=True)
    otroDia = models.CharField(verbose_name = "Otro Diagnóstico", max_length=50, null=True, blank=True)
    
    paciente = models.ForeignKey(Paciente, verbose_name="Paciente", on_delete=models.SET_NULL, null=True, blank=True)
    edadAnio = models.PositiveIntegerField(verbose_name="Edad (años)", null=True, blank=True)
    edadMes = models.PositiveIntegerField(verbose_name="Edad (meses)", null=True, blank=True)
    edadDia = models.PositiveIntegerField(verbose_name="Edad (días)", null=True, blank=True)
    
    
    
    fechaIn3 = models.DateField(verbose_name = "Fecha inicio de signos")
    signoSint3 = models.TextField(verbose_name = "Signos y sintomas")
    
    
    tratamiento3 = models.TextField(verbose_name = "Tratamiento")
    boolLab = models.BooleanField(verbose_name = "Ya se registro laboratorio", default=False)
    boolFinalizado = models.BooleanField(verbose_name = "Finalizado", default=False)
    
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
    otrosFuentes = models.CharField(verbose_name="Otras fuentes",max_length=200, null=True, blank=True)
    
    personaPersona = models.CharField(verbose_name="Persona a persona", max_length=20, choices=OTRA_PERSONA_OPCIONES)
    aerea = models.CharField(verbose_name="Aerea", max_length=20, choices=OTRA_PERSONA_OPCIONES)
    digestiva = models.CharField(verbose_name="Digestiva", max_length=20, choices=OTRA_PERSONA_OPCIONES)
    fomitesMec = models.CharField(verbose_name="Fomites", max_length=20, choices=OTRA_PERSONA_OPCIONES)
    vectores = models.CharField(verbose_name="Vectores", max_length=20, choices=OTRA_PERSONA_OPCIONES)
    otrosMecanismos = models.CharField(verbose_name="Otras mecanismos",max_length=200, null=True, blank=True)
    

class Estudio(models.Model):
    nombre = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    tipo = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    fecha = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    resultado = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    registroEstudio=models.ForeignKey(RegistroEstudio, on_delete=models.CASCADE)
    
class Logos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=250, blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True, verbose_name="ImagenLogo")
    actualizado = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.logo.path)

        if img.height > 85:
            output_size = (None,85)
            img.thumbanail(output_size, Image.LANCZOS)
            img.save(self.logo.path)

class NotificacionBrote(models.Model):
    folio = models.CharField(verbose_name = "Folio", max_length=50, null=True, blank=True, unique=True)
    unidadNot = models.ForeignKey(Unidad, verbose_name="Unidad notificante", on_delete=models.SET_NULL, null=True, blank=True)
    fechaNot = models.DateField(verbose_name = "Fecha Notificacion", default=timezone.now)
    fechaEstudio = models.DateField(verbose_name = "Fecha Inicio Estudio", null=True, blank=True)
    DiaProHep = models.CharField(verbose_name='Diagnóstico Probable', max_length=1, choices=HEPATITIS_CHOICES, null=True, blank=True)
    DiaFin = models.CharField(verbose_name = "Diagnóstico Final", max_length=1, choices=HEPATITIS_CHOICES, null=True, blank=True)

    DiaProHep2 = models.CharField(verbose_name='Diagnóstico Probable', max_length=1, choices=HEPATITIS_CHOICES, null=True, blank=True)
    DiaFin2 = models.CharField(verbose_name = "Diagnóstico Final", max_length=1, choices=HEPATITIS_CHOICES, null=True, blank=True)
    fechaNot2 = models.DateField(verbose_name = "Fecha Notificacion", default=timezone.now)
    fechaNot3 = models.DateField(verbose_name = "Fecha Notificacion", default=timezone.now)
    casosProbables = models.CharField(verbose_name = "Fecha Notificacion", max_length=50,null=True, blank=True)
    casosConfirmados = models.CharField(verbose_name = "Fecha Notificacion", max_length=50,null=True, blank=True)
    hospitalizados = models.CharField(verbose_name = "Fecha Notificacion", max_length=50,null=True, blank=True)

    anteEpiBrote = models.CharField(verbose_name = "Fecha Notificacion", max_length=50,null=True, blank=True)
    probFuenBrote = models.CharField(verbose_name = "Fecha Notificacion", max_length=50,null=True, blank=True)
    probMecTransmision = models.CharField(verbose_name = "Fecha Notificacion", max_length=50,null=True, blank=True)

    accionesPrevControl = models.CharField(verbose_name = "Fecha Notificacion", max_length=50,null=True, blank=True)


class DistribucionGeografica(models.Model):
    area = models.CharField(verbose_name = "Área, Manzana, Colonia, Localidad, Escuela, Guardería O Vivienda", max_length=50,null=True, blank=True)
    numeroCasos = models.CharField(verbose_name = "Fecha Notificacion", max_length=50,null=True, blank=True)   
    numeroDefunciones = models.CharField(verbose_name = "Fecha Notificacion", max_length=50,null=True, blank=True)
    notificacionBrote = models.ForeignKey(NotificacionBrote, on_delete=models.CASCADE)

class Anexo8(models.Model):
    nombreFallecido = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    fechaDefuncion = models.DateField(verbose_name = "Fecha de defunción", null=True, blank=True)
    escolaridad = models.CharField(verbose_name='Escolaridad', max_length=10, choices=ESCOLARIDAD_CHOICES, null=True, blank=True)
    ocupacion = models.CharField(verbose_name='Ocupación', max_length=30, null=True, blank=True)
    lugardeResidenciaMuni = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    lugardeResidenciaEnti = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    lugarDefMuni = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='municipioDef')
    lugarDefEnti = models.ForeignKey(Entidad, on_delete=models.CASCADE, related_name='entidadDef')
    nombreCertificante = models.CharField(verbose_name="Nombre del Certificante", max_length=20)

    causasDef = models.CharField(verbose_name="Causas de defunción", max_length=200)
    causasDef2 = models.CharField(verbose_name="Causas de defunción2", max_length=100)
    causaVigEpi = models.CharField(verbose_name="Causa sujeta a vigilancia epidemiologica", max_length=100)

    ratifica = models.CharField(verbose_name="Ratifica", max_length=100, choices=RATIFICA_CHOICES, null=True, blank=True)
    causaVigEpi2 = models.CharField(verbose_name="Causa sujeta a vigilancia epidemiologica", max_length=100)
    causasDef3 = models.CharField(verbose_name="Causas de defunción3", max_length=200)
    causasDef4 = models.CharField(verbose_name="Causas de defunción4", max_length=100)
    fechaRecoleccion = models.DateField(verbose_name = "Fecha de recolección", null=True, blank=True)
    fechaInicio = models.DateField(verbose_name = "Fecha de inicio", null=True, blank=True)
    fechaConclusion = models.DateField(verbose_name = "Fecha de conclusión", null=True, blank=True)
    reporteInegi = models.DateField(verbose_name = "Fecha de reporte a INEGI", null=True, blank=True)
    observaciones = models.CharField(verbose_name="Observaciones", max_length=200, null=True, blank=True)
    nombreResponsableInv = models.CharField(verbose_name="Nombre del responsable de la investigación", max_length=50, null=True, blank=True)
    cargo = models.CharField(verbose_name="Cargo", max_length=50, null=True, blank=True)
    firma = models.CharField(verbose_name="Firma", max_length=50, null=True, blank=True)

    tipoDocumento = models.CharField(verbose_name="Tipo de documento", max_length=50, null=True, blank=True)
    numPaquete = models.CharField(verbose_name="Número de paquete", max_length=50, null=True, blank=True)
    numActa = models.CharField(verbose_name="Número de acta", max_length=50, null=True, blank=True)
    folioCaptura = models.CharField(verbose_name="Folio de captura", max_length=50, null=True, blank=True)
    nombreCodificador = models.CharField(verbose_name="Nombre del codificador", max_length=50, null=True, blank=True)
    