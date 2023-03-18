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
        if user == request.user:
            post_values = request.POST.copy()
            group_ids = post_values.getlist('groups') # Obtener la lista de grupos seleccionados por el usuario
            rolDirector = Group.objects.get(name = 'Director')
            if rolDirector.id not in group_ids: # Verificar si el grupo "Director" no está ya en la lista
                group_ids.append(rolDirector.id) # Agregar el grupo "Director" a la lista
            post_values.setlist('groups', group_ids) # Actualizar el valor de "groups" en el diccionario POST
            form = GroupAssignForm(post_values, instance=user)
            if form.is_valid():
                form.save()
                return render(request, 'home/Director/assign_groups.html', {
                    'segment': 'Lista_Usuarios_Director',
                    'form': form,
                    'msg': 'Se ha guardado con exito',
                    'msgType': 'success'
                })
        else:
            form = GroupAssignForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
            group_ids = list(user.groups.all().values_list('id', flat=True))
            initial = {'groups': group_ids}
            # form = GroupAssignForm(initial=initial, instance=user)
            form.fields['groups'].choices=[(group.id, group.name) for group in Group.objects.all().exclude(name = 'Director')]
            return render(request, 'home/Director/assign_groups.html', {
                'segment': 'Lista_Usuarios_Director',
                'form': form,
                'msg': 'Se ha guardado con exito',
                'msgType': 'success'
            })
    else:
        group_ids = list(user.groups.all().values_list('id', flat=True))
        initial = {'groups': group_ids}
        form = GroupAssignForm(initial=initial, instance=user)
        if user != request.user:
            form.fields['groups'].choices=[(group.id, group.name) for group in Group.objects.all().exclude(name = 'Director')]
        return render(request, 'home/Director/assign_groups.html', {
            'segment': 'Lista_Usuarios_Director',
            'form': form,
            })