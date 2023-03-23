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
    Instituciones = Institucion.objects.all()
    mensaje = None
    msgType = None
    if msg == 'Exito create insti':
        mensaje = 'Institucion creada con exito!'
        msgType = 'success'
    elif msg == 'prueba2':
        mensaje = 'Mensaje 2 de prueba'
        msgType = 'danger'
        
    context = {
        'segment': 'CRUD_tablas',
        'mensaje':mensaje,
        'msg': mensaje,
        'msgType': msgType,
        'formAddJurisdiccion' : formAddJurisdiccion,
        'formAddInstitucion' : formAddInstitucion,
        'Instituciones' : Instituciones
    }
    
    return render(request, 'home/Director/CRUDTablas.html', context)