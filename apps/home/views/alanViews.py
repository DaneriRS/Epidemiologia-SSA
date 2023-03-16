from django.contrib.auth.decorators import login_required
from django.shortcuts import render
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
@roles_required(['Director'], redirect_url='home')
def lista_usuarios(request):
    usuarios = User.objects.all()
    extras = InformacionUsuario.objects.all()
    print(request.user.is_encarUni())
    return render(request, 'home/Director/lista_usuarios.html', {
        'segment': 'Lista_Usuarios_Director',
        'usuarios': usuarios,
        'extras': extras,
    })

@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def assign_groups(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = GroupAssignForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = GroupAssignForm(instance=user)
    return render(request, 'home/Director/assign_groups.html', {'form': form})