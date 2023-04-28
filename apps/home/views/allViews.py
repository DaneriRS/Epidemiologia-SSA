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
    formExeclLocalidad = ExcelLocalidadForm()
    formExcelMunicipio= ExcelMunicipioForm()
    formExcelUMedicas = ExcelUMedicasForm()
    
    formAddMunicipio = MunicipioForm(auto_id="addMunicipio_%s")
    formEditMunicipio = MunicipioForm(auto_id="editMunicipio_%s")
    formAddLocalidad = LocalidadForm(auto_id="addLocalidad_%s")
    formEditLocalidad = LocalidadForm(auto_id="editLocalidad_%s")
    formAddTipologia = TipologiaForm(auto_id="addTipologia_%s")
    formEditTipologia = TipologiaForm(auto_id="editTipologia_%s")
    formAddJurisdiccion = JurisdiccionForm(auto_id="addJurisdiccion_%s")
    formEditJurisdiccion = JurisdiccionForm(auto_id="editJurisdiccion_%s")
    formAddInstitucion = InstitucionForm(auto_id="addInstitucion_%s")
    formEditInstitucion = InstitucionForm(auto_id="editInstitucion_%s")
    
    formAddEntidad = EntidadForm(auto_id="addEntidad_%s")
    formEditEntidad = EntidadForm(auto_id="editEntidad_%s")
    formAddEstablecimiento = EstablecimientoForm(auto_id="addEstablecimiento_%s")
    formEditEstablecimiento = EstablecimientoForm(auto_id="editEstablecimiento_%s")
    
    Instituciones = Institucion.objects.all()
    Localidades = Localidad.objects.all()
    Municipios = Municipio.objects.all()
    Umedicas = Unidad.objects.all()
    Entidades = Entidad.objects.all()
    Establecimientos = Establecimiento.objects.all()
    Tipologias = Tipologia.objects.all()
    Jurisdicciones = Jurisdiccion.objects.all()

    mensaje = None
    msgType = None
    presionar = False
    btnPresionar = None
    if msg == 'Exito create insti':
        mensaje = 'Institucion creada con exito!'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Institucion'
    elif msg == 'exitoAddEntidad':
        mensaje = 'Entidad Registrada con exito!'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Entidad'
    elif msg == 'errorAddEntidad':
        mensaje = '¡ERROR Entidad NO Registrada!'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Entidad'
    elif msg == 'errorExistEntidad':
        mensaje = '¡ERROR! Entidad no existe'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Entidad'
    elif msg == 'exitoEditEntidad':
        mensaje = 'Entidad Editada con exito!'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Entidad'
    elif msg == 'exitoDelEntidad':
        mensaje = 'Entidad Eliminada con exito!'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Entidad'
    elif msg == 'uniqueAddEntidad':
        mensaje = '¡ERROR La clave de Entidad ya existe!'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Entidad'
    elif msg == 'exitoAddEstablecimiento':
        mensaje = 'Establecimiento Registrada con exito!'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Establecimiento'
    elif msg == 'errorAddEstablecimiento':
        mensaje = '¡ERROR Establecimiento NO Registrado!'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Establecimiento'
    elif msg == 'errorExistEstablecimiento':
        mensaje = '¡ERROR! Establecimiento no existe'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Establecimiento'
    elif msg == 'exitoEditEstablecimiento':
        mensaje = 'Establecimiento Editado con exito!'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Establecimiento'
    elif msg == 'exitoEditEstablecimiento':
        mensaje = '¡ERROR Establecimiento NO Editado!'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Establecimiento'
    elif msg == 'exitoDelEstablecimiento':
        mensaje = 'Establecimiento Eliminadao con exito!'
    elif msg == 'exitoDelEstablecimiento':
        mensaje = '¡ERROR Establecimiento NO Eliminado!'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Establecimiento'
    elif msg == 'Exito Registro Excel':
        mensaje = 'Registros Realizados con Exito'
        msgType = 'success'
    elif msg == 'Error Registro Excel':
        mensaje = '¡ERROR! Registros no Realizados'
        msgType = 'danger'
    elif msg == 'errorAddedMunicipio':
        mensaje = '¡ERROR! Municipio no creado'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Municipio'
    elif msg == 'exitoAddedMunicipio':
        mensaje = '¡Exito! Municipio creado'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Municipio'
    elif msg == 'errorExistMunicipio':
        mensaje = '¡ERROR! Municipio no existe'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Municipio'
    elif msg == 'exitoAditedMunicipio':
        mensaje = '¡Exito! Municipio editado'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Municipio'
    elif msg == 'errorAditedMunicipio':
        mensaje = '¡ERROR! Municipio no editado'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Municipio'
    elif msg == 'exitoDeletedMunicipio':
        mensaje = '¡Exito! Municipio eliminado'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Municipio'
    elif msg == 'errorDeletedMunicipio':
        mensaje = '¡ERROR! Municipio no eliminado'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Municipio'
    elif msg == 'uniqueAddedMunicipio':
        mensaje = '¡ERROR La clave de Municipio ya existe!'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Municipio'
    elif msg == 'errorAddedLocalidad':
        mensaje = '¡ERROR! Localidad no creada'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Localidad'
    elif msg == 'exitoAddedLocalidad':
        mensaje = '¡Exito! Localidad creada'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Localidad'
    elif msg == 'errorExistLocalidad':
        mensaje = '¡ERROR! Localidad no existe'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Localidad'
    elif msg == 'exitoAditedLocalidad':
        mensaje = '¡Exito! Localidad editada'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Localidad'
    elif msg == 'errorAditedLocalidad':
        mensaje = '¡ERROR! Localidad no editada'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Localidad'
    elif msg == 'exitoDeletedLocalidad':
        mensaje = '¡Exito! Localidad eliminada'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Localidad'
    elif msg == 'errorDeletedLocalidad':
        mensaje = '¡ERROR! Localidad no eliminada'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Localidad'
    elif msg == 'uniqueAddedLocalidad':
        mensaje = '¡ERROR La clave de Localidad ya existe!'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Localidad'
    elif msg == 'errorAddedTipologia':
        mensaje = '¡ERROR! Tipologia no creada'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Tipologia'
    elif msg == 'exitoAddedTipologia':
        mensaje = '¡Exito! Tipologia creada'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Tipologia'
    elif msg == 'errorExistTipologia':
        mensaje = '¡ERROR! Tipologia no existe'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Tipologia'
    elif msg == 'exitoAditedTipologia':
        mensaje = '¡Exito! Tipologia editada'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Tipologia'
    elif msg == 'errorAditedTipologia':
        mensaje = '¡ERROR! Tipologia no editada'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Tipologia'
    elif msg == 'exitoDeletedTipologia':
        mensaje = '¡Exito! Tipologia eliminada'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Tipologia'
    elif msg == 'errorDeletedTipologia':
        mensaje = '¡ERROR! Tipologia no eliminada'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Tipologia'
    elif msg == 'uniqueAddedTipologia':
        mensaje = '¡ERROR La clave de Tipologia ya existe!'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Tipologia'
    elif msg == 'errorAddedJurisdiccion':
        mensaje = '¡ERROR! Jurisdiccion no creado'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Jurisdiccion'
    elif msg == 'exitoAddedJurisdiccion':
        mensaje = '¡Exito! Jurisdiccion creado'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Jurisdiccion'
    elif msg == 'errorExistJurisdiccion':
        mensaje = '¡ERROR! Jurisdiccion no existe'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Jurisdiccion'
    elif msg == 'exitoAditedJurisdiccion':
        mensaje = '¡Exito! Jurisdiccion editado'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Jurisdiccion'
    elif msg == 'errorAditedJurisdiccion':
        mensaje = '¡ERROR! Jurisdiccion no editado'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Jurisdiccion'
    elif msg == 'exitoDeletedJurisdiccion':
        mensaje = '¡Exito! Jurisdiccion eliminado'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Jurisdiccion'
    elif msg == 'errorDeletedJurisdiccion':
        mensaje = '¡ERROR! Jurisdiccion no eliminado'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Jurisdiccion'
    elif msg == 'uniqueAddedJurisdiccion':
        mensaje = '¡ERROR La clave de Jurisdiccion ya existe!'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Jurisdiccion'
    elif msg == 'errorAddedInstitucion':
        mensaje = '¡ERROR! Institucion no creado'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Institucion'
    elif msg == 'exitoAddedInstitucion':
        mensaje = '¡Exito! Institucion creado'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Institucion'
    elif msg == 'errorExistInstitucion':
        mensaje = '¡ERROR! Institucion no existe'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Institucion'
    elif msg == 'exitoAditedInstitucion':
        mensaje = '¡Exito! Institucion editado'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Institucion'
    elif msg == 'errorAditedInstitucion':
        mensaje = '¡ERROR! Institucion no editado'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Institucion'
    elif msg == 'exitoDeletedInstitucion':
        mensaje = '¡Exito! Institucion eliminado'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Institucion'
    elif msg == 'errorDeletedInstitucion':
        mensaje = '¡ERROR! Institucion no eliminado'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Institucion'
    elif msg == 'uniqueAddedInstitucion':
        mensaje = '¡ERROR La clave de Institucion ya existe!'
        msgType = 'danger'
        presionar = True
        btnPresionar = 'Institucion'
        
        
    context = {
        'segment': 'CRUD_tablas',
        'mensaje':mensaje,
        'msg': mensaje,
        'msgType': msgType,
        'formAddJurisdiccion' : formAddJurisdiccion,
        'formEditJurisdiccion' : formEditJurisdiccion,
        'formAddEntidad': formAddEntidad,
        'formEditEntidad': formEditEntidad,
        'formAddEstablecimiento': formAddEstablecimiento,
        'formEditEstablecimiento': formEditEstablecimiento,
        'formExcelLocalidad' : formExeclLocalidad,
        'formExcelMunicipio' : formExcelMunicipio,
        'formExcelUMedicas' : formExcelUMedicas,
        'Instituciones' : Instituciones,
        'Localidades': Localidades,
        'Municipios' : Municipios,
        'Umedicas' : Umedicas,
        'Entidades' : Entidades,
        'Establecimientos' : Establecimientos,
        'Tipologias' : Tipologias,
        'Jurisdicciones' : Jurisdicciones,
        'formAddMunicipio' : formAddMunicipio,
        'formEditMunicipio' : formEditMunicipio,
        'formAddLocalidad' : formAddLocalidad,
        'formEditLocalidad' : formEditLocalidad,
        'formAddTipologia' : formAddTipologia,
        'formEditTipologia' : formEditTipologia,
        'formAddInstitucion' : formAddInstitucion,
        'formEditInstitucion' : formEditInstitucion,
        'presionar' : presionar,
        'btnPresionar' : btnPresionar,
    }
    
    return render(request, 'home/Director/CRUDTablas.html', context)

@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def vista_logos(request, msg):
    formEditLogos = LogosForm(auto_id="editLogos_%s")
    Logo = Logos.objects.all()

    mensaje = None
    msgType = None
    presionar = False
    btnPresionar = None
    if msg == 'exitoEditLogo':
        mensaje = 'Logo Editado con exito!'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Logo'
    elif msg == 'exitoDelLogo':
        mensaje = 'Logo Eliminado con exito!'
        msgType = 'success'
        presionar = True
        btnPresionar = 'Logo'

    context = {
        'segment': 'Logos_tabla',
        'mensaje':mensaje,
        'msg': mensaje,
        'Logos' : Logos,
        'formEditLogos' : formEditLogos,
        'presionar' : presionar,
        'btnPresionar' : btnPresionar,
    }
    return render(request, 'home/Director/actualizarLogos.html', context)