# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import pandas as pd
from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from formtools.wizard.views import *
from django.forms import formset_factory


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

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
    
@login_required
def import_excel(request):
    form=ExcelForm()
    form2=IndividualForm()
    if request.method == 'POST' and "Excel" in request.POST:
        excel_file = request.FILES['Subir_Excel']
        df = pd.read_excel(excel_file)

        try:
            # Itera a través de cada fila del DataFrame
            for index, row in df.iterrows():
                # Crea una instancia del modelo con los datos de la fila
                obj = User(
                    username=row['username'],
                    first_name=row['nombre'],
                    last_name=row['apellidos'],
                    email=row['correo'],
                    password=make_password(row['password']),
                    # Continúa agregando todos los campos del modelo que quieras importar
                )
                # Guarda la instancia del modelo en la base de datos
                obj.save()
            print('todo bien')
            return render(request, 'home/registrar_excel.html',{
                'form': form,
                'form2': form2
            })
        except:
            print('error')
            return render(request, 'home/registrar_excel.html',{
                'form': form,
                'form2': form2
            })
    if request.method == 'POST' and "Individual" in request.POST:
        obj = User(
            username=request.POST['Usuario'],
            first_name=request.POST['Nombre'],
            last_name=request.POST['Apellidos'],
            email=request.POST['Correo'],
            password=make_password(request.POST['Contraseña']),
        )
        obj.save()
        return render(request, 'home/registrar_excel.html',{
            'form': form,
            'form2': form2
        })
    else:
        return render(request, 'home/registrar_excel.html',{
            'form': form,
            'form2': form2
        })


def multiForm(request):
    return render(request, "home/exampleForm.html")

class BookingWizzadView(CookieWizardView):
    form_list = [ContactForm1, ContactForm2, ContactForm3]
    template_name = 'home/exampleForm.html'

    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        return HttpResponse("Enviado")
    
@login_required    
def nuevoPaciente(request):
    if request.method == 'POST':
        formA = registroPaciente(request.POST)
        form = registroPaciente()
        if formA.is_valid():
            try:
                formA.save()
                return render(request, 'home/nuevoPaciente.html', {
                'form': form,
                'msg' : "1"
                })
            except:
                return render(request, 'home/nuevoPaciente.html', {
                'form': form,
                'msg' : "0"
                })
    else:
        form = registroPaciente()
    
    return render(request, 'home/nuevoPaciente.html', {'form': form})