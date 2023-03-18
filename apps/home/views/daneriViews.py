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


#@login_required
def user(request):
    form = User(request.POST)
    if request.method == "POST":
        form = lista_usuarios(request.post)
        obj = User(
            username=request.POST['Usuario'],
            first_name=request.POST['Nombre'],
            last_name=request.POST['Apellidos'],
            email=request.POST['Correo'],
            password=make_password(request.POST['Contraseña']),
        )
        obj.save()
    return render(request, "home/user.html", {'form': form,'segment': 'Lista_Usuarios_Director', 'msg': 'Se ha guardado con exito',
                    'msgType': 'success'})


def user(request):
    form = User(request.POST or None)
    if request.method == "POST":
        form = assign_groups (request.post)
    return render(request, "home/user.html", {'form': form})
