from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
import pandas as pd
from django.shortcuts import get_object_or_404, render
from apps.home.models import *
from apps.home.forms.allForms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

def roles_required(roles, redirect_url=None):
    def decorator(view_func):
        @user_passes_test(lambda user: user.groups.filter(name__in=roles).exists(), login_url=redirect_url)
        def wrapper(request, *args, **kwargs):
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


@login_required(login_url="/login/")
#@permission_required('User.can_edit')
def user(request, user_id):
    user = User.objects.get(pk=user_id)
    #form = userProfileForm(request.POST)
    if request.method == "POST":
        form = userProfileForm(request, instance=user)
        if form.is_valid():
            form.save()
    return render(request, "home/user.html", {'form': 'form', 'msg': 'Se ha guardado con exito',
                    'msgType': 'success'})





def addEntidadCRUD(request):
    formAddEntidad = addEntidad()
    formAddEstablecimiento = addEstablecimiento()
    if request.method == 'POST':
        form = addEstablecimiento(request.POST)
        if form.is_valid():
            try:
                form.save()
                mensaje = None
                msgType = None
                mensaje = 'Mensaje 1 de prueba'
                msgType = 'success'
                context = {
                    'segment': 'CRUD_tablas',
                    'mensaje':mensaje,
                    'msg': mensaje,
                    'msgType': msgType,
                    'formAddJurisdiccion' : formAddJurisdiccion,
                    'formAddInstitucion' : formAddInstitucion
                }
                return render(request, 'home/Director/CRUDTablas.html', context)
                #return redirect(reverse('vista_tablas', kwargs={'msg':'Exito creado Entidad'}))
            except:
                print('error')

def delEntidad(request, pk):
    formAddEntidad = addEntidad()
    formAddEstablecimiento = addEstablecimiento()

    try:
        estb = Establecimiento.objects.get(id=pk)
        estb.delete()
    except:
        print("error")

    mensaje = None
    msgType = None
    mensaje = 'Mensaje 1 de prueba'
    msgType = 'success'
    context = {
        'segment': 'CRUD_tablas',
        'mensaje':mensaje,
        'msg': mensaje,
        'msgType': msgType,
        'formAddEntidad' : formAddEntidad,
        'formAddEstablecimiento' : formAddEstablecimiento
    }
    return render(request, 'home/Director/CRUDTablas.html', context)

