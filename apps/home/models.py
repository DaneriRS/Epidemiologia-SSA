# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

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
    # coloniaLocalidad = models.CharField(verbose_name = "Colonia o localidad", max_length=5, choices=COLLOC)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    # idMunicipio = models.CharField(verbose_name = "Municipio", max_length=5, choices=MUNICIPIOS)
    # idEntidad = models.CharField(verbose_name = "Entidad", max_length=2, choices=ENTIDADES) 
    codigoPostal = models.CharField(verbose_name = "Codigo postal", max_length=5)
    telefonoPaciente = models.CharField(verbose_name = "Telefono", max_length = 10)

class RegistroEstudio(models.Model):
    folio = models.CharField(verbose_name = "Folio", max_length=50, null=True, blank=True, unique=True)
    unidadNot = models.CharField(verbose_name = "unidad Notificante", max_length=50, null=True, blank=True)
    local = models.CharField(verbose_name = "Localidad", max_length=50,null=True, blank=True)
    entOdEL = models.CharField(verbose_name = "Entidad", max_length=50,null=True, blank=True)
    cvClue = models.CharField(verbose_name = "claveClue", max_length=50,null=True, blank=True)
    municipio1 = models.CharField(verbose_name = "Municipio", max_length=50,null=True, blank=True)
    institucion = models.CharField(verbose_name = "Institucion", max_length=50,null=True, blank=True)
    cvSuUni = models.CharField(verbose_name = "claveSuave", max_length=50,null=True, blank=True)
    jurisdicEq = models.CharField(verbose_name = "Jurisdiccion", max_length=50,null=True, blank=True)
    fechaNot = models.CharField(verbose_name = "Fecha Notificacion", max_length=50,null=True, blank=True)
    fechaIni = models.CharField(verbose_name = "Fecha Inicio Estudio", max_length=50,null=True, blank=True)
    fechaFin = models.CharField(verbose_name = "Fecha Fin Estudio", max_length=50,null=True, blank=True)
    DiaProHep = models.CharField(verbose_name = "diagnosticoProbable", max_length=50,null=True, blank=True)
    DiaFin = models.CharField(verbose_name = "diagnosticoFinal", max_length=50,null=True, blank=True)
    otroDia = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)

    noAfili = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    nombre = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    ap = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    am = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    sexo = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    fechaNac = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    anos = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    meses = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    dias = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    calle = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    num = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    colonia = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    municipio2 = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    cvMun2 = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    ent2 = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    cvEnt2 = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    cp2 = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    tel2 = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    
    fechaIn3 = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    signoSint3 = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    tratamiento3 = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    
    def __str__(self):
        return self.folio + ' - ' + self.unidadNot

class Estudio(models.Model):
    nombre = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    tipo = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    fecha = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    resultado = models.CharField(verbose_name = "otroDiagnostico", max_length=50,null=True, blank=True)
    registroEstudio=models.ForeignKey(RegistroEstudio, on_delete=models.CASCADE)
    