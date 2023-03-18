from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render
from apps.home.models import *
from apps.home.forms.allForms import *

def roles_required(roles, redirect_url=None):
    def decorator(view_func):
        @user_passes_test(lambda user: user.groups.filter(name__in=roles).exists(), login_url=redirect_url)
        def wrapper(request, *args, **kwargs):
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


@login_required(login_url="/login/")
def user(request):
    #user = get_object_or_404(User)
    form = GroupAssignForm(request.POST)
    if request.method == "POST":
        form = GroupAssignForm(request.post)
        obj = User(
            username=request.POST['Usuario'],
            first_name=request.POST['Nombre'],
            last_name=request.POST['Apellidos'],
            email=request.POST['Correo'],
            password=make_password(request.POST['Contraseña']),
        )
        obj.save()
        form.save()
    return render(request, "home/user.html", {'form': form, 'msg': 'Se ha guardado con exito',
                    'msgType': 'success'})


@login_required(login_url="/login/")
def actualizar(request, user_id):
    user = get_object_or_404(User, id= user_id)
    form=User()
    #form2=unidadPerfil()
    #form = User(initial={'usuario'= username,'Nombre' =first_name, 'Apellidos'=last_name , 'Correo'= email 'Contraseña'= password,'ap'})
    form= unidadPerfil(initial={
        'unidad': Unidad.__name__,
        'claveclues': Unidad.claveclues,
        'jurisdiccion': Jurisdiccion.clave,
        'municipio': Municipio.__name__,
        'entidad': Entidad.nombre})
    if request.method == "POST":
        form = unidadPerfil(request.POST)
        if form.is_valid():
            unidadPerfil.save()
            return render(request, 'home/user.html', {
                'form': form,
                'msg': 'Se ha guardado con exito',
                'msgType': 'EXITO'})
        else: 
            return render(request, 'home/user.html', {
                'form': form,
                'msg': 'No se ha guardado',
                'msgType': 'FALLO'})

    return render(request, "home/user.html", {'form': form})
    

