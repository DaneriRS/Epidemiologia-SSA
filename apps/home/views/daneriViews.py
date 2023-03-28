from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
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

''' #################    USUARIO  #################'''
@login_required(login_url="/login/")
#@permission_required('User.can_edit')
def user(request):
    user = User.objects.get(id=request.user.id)
    #form = userProfileForm(request.POST)
    if request.method == "POST":
        form = userProfileform(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return render(request, "home/user.html", {'form': form, 'msg': 'Se ha guardado con exito',
                        'msgType': 'success'})
    else:
        form = userProfileform(instance=user)
        return render(request, "home/user.html", {'form': form, 'msg': 'Se ha guardado con exito',
                    'msgType': 'success'})


''' #################    CRUD ENTIDAD  #################'''

@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def addEntidad(request):
    #formAddEntidad = addEntidad()
    if request.method == 'POST':
        form = EntidadForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                '''mensaje = None
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
                '''#return render(request, 'home/Director/CRUDTablas.html', context)
                return redirect(reverse('vista_tablas', kwargs={'msg':'exitoAddEntidad'}))
            except:
                '''context = {
                    'segment': 'CRUD_tablas',
                    'mensaje':mensaje,
                    'msg': mensaje,
                    'msgType': msgType,
                    'formAddEntidad' : formAddEntidad,
                    'formAddEstablecimiento' : formAddEstablecimiento
                }'''
                return redirect(reverse('vista_tablas', kwargs={'msg':'errorAddEntidad'}))
        else:
            return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))

@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def editEntidad(request):
    #formAddEntidad = addEntidad()
    if request.method == 'POST':
        try:
            entity = Entidad.objects.get(id = pk)
        except Exception as e:
                return redirect(reverse('vista_tablas', kwargs={'msg':'errorExistEntidad'}))
        form = EntidadForm(request.POST, instance=entity)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse('vista_tablas', kwargs={'msg':'exitoEditEntidad'}))
            except:
                return redirect(reverse('vista_tablas', kwargs={'msg':'errorEditEntidad'}))
        else:
            return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))


@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def delEntidad(request, pk):
    try:
        entity = Entidad.objects.get(id=pk)
    except:
        return redirect(reverse('vista_tablas', kwargs={'msg':'exitoEditEntidad'}))

    try:
        entity.delete()
        return redirect(reverse('vista_tablas', kwargs={'msg':'exitoDelEntidad'}))
    except Exception as e:
        return redirect(reverse('vista_tablas', kwargs={'msg':'errorDelEntidad'}))


''' #################    CRUD ESTABLECIMIENTO  #################'''

@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def addEstablecimiento(request):
    #formAddEstablecimiento = addEstablecimiento()
    if request.method == 'POST':
        form = EstablecimientoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse('vista_tablas', kwargs={'msg':'exitoAddEstablecimiento'}))
            except:
                return redirect(reverse('vista_tablas', kwargs={'msg':'errorAddEstablecimiento'}))
        else:
            return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))

@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def editEstablecimiento(request):
    if request.method == 'POST':
        try:
            entity = Establecimiento.objects.get(id = pk)
        except Exception as e:
                return redirect(reverse('vista_tablas', kwargs={'msg':'errorExistEstablecimiento'}))
        form = EstablecimientoForm(request.POST, instance=entity)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse('vista_tablas', kwargs={'msg':'exitoEditEstablecimiento'}))
            except:
                return redirect(reverse('vista_tablas', kwargs={'msg':'errorEditEstablecimiento'}))
        else:
            return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))


@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def delEstablecimiento(request, pk):
    try:
        entity = Establecimiento.objects.get(id=pk)
    except:
        return redirect(reverse('vista_tablas', kwargs={'msg':'errorEditEstablecimiento'}))

    try:
        entity.delete()
        return redirect(reverse('vista_tablas', kwargs={'msg':'exitoDelEstablecimiento'}))
    except Exception as e:
        return redirect(reverse('vista_tablas', kwargs={'msg':'errorDelEstablecimiento'}))
