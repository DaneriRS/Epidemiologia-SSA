# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.home.models import *
from .alanViews import *
from .angelViews import *
from .ulisesViews import *
from .daneriViews import *


@login_required(login_url="/login/")
def index(request):
    
    mensaje = 'Bienvenido de nuevo!'
    msgType = 'success'
    context = {
        'segment': 'index',
        'mensaje':mensaje,
        'msg': mensaje,
        'msgType': msgType,
    }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def vista_tablas(request, msg):
    formAddJurisdiccion = addJurisdiccion()
    formAddInstitucion = addInstitucion()
    formAddEntidad = addEntidad()
    formAddEstablecimiento = addEstablecimiento()
    formdelEntidad = addEntidad()
    formdelEstablecimiento = addEstablecimiento()
    formExeclLocalidad = ExcelLocalidadForm()
    formExcelMunicipio= ExcelMunicipioForm()
    formExcelUMedicas = ExcelUMedicasForm()
    
    formAddMunicipio = MunicipioForm(auto_id="addMunicipio_%s")
    formEditMunicipio = MunicipioForm(auto_id="editMunicipio_%s")
    
    Instituciones = Institucion.objects.all()
    Localidades = Localidad.objects.all()
    Municipios = Municipio.objects.all()
    Umedicas = Unidad.objects.all()
    Entidades = Entidad.objects.all()
    mensaje = None
    msgType = None
    if msg == 'Exito create insti':
        mensaje = 'Institucion creada con exito!'
        msgType = 'success'
    elif msg == 'Exito Registro creado':
        mensaje = 'Registro creado con exito!'
        msgType = 'success'
    elif msg == 'Error al crear':
        mensaje = 'Error no creado!'
        msgType = 'success'
    elif msg == 'Exito Registro Excel':
        mensaje = 'Registros Realizados con Exito'
        msgType = 'success'
    elif msg == 'Error Registro Excel':
        mensaje = '¡ERROR! Registros no Realizados'
        msgType = 'danger'
    elif msg == 'errorAddedMunicipio':
        mensaje = '¡ERROR! Municipio no creado'
        msgType = 'danger'
    elif msg == 'exitoAddedMunicipio':
        mensaje = '¡Exito! Municipio creado'
        msgType = 'success'
    elif msg == 'errorExistMunicipio':
        mensaje = '¡ERROR! Municipio no existe'
        msgType = 'danger'
    elif msg == 'exitoAditedMunicipio':
        mensaje = '¡Exito! Municipio editado'
        msgType = 'success'
    elif msg == 'errorAditedMunicipio':
        mensaje = '¡ERROR! Municipio no editado'
        msgType = 'danger'
    elif msg == 'exitoDeletedMunicipio':
        mensaje = '¡Exito! Municipio eliminado'
        msgType = 'success'
    elif msg == 'errorDeletedMunicipio':
        mensaje = '¡ERROR! Municipio no eliminado'
        msgType = 'danger'
        
    context = {
        'segment': 'CRUD_tablas',
        'mensaje':mensaje,
        'msg': mensaje,
        'msgType': msgType,
        'formAddJurisdiccion' : formAddJurisdiccion,
        'formAddInstitucion' : formAddInstitucion,
        'formAddEntidad': formAddEntidad,
        'formAddEstablecimiento': formAddEstablecimiento,
        'formExcelLocalidad' : formExeclLocalidad,
        'formExcelMunicipio' : formExcelMunicipio,
        'formExcelUMedicas' : formExcelUMedicas,
        'Instituciones' : Instituciones,
        'Localidades': Localidades,
        'Municipios' : Municipios,
        'Umedicas' : Umedicas,
        'Entidades' : Entidades,
        'formAddMunicipio' : formAddMunicipio,
        'formEditMunicipio' : formEditMunicipio,
    }
    
    return render(request, 'home/Director/CRUDTablas.html', context)