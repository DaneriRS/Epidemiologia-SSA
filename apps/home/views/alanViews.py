from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
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
def editar_usuarios(request, user_id):
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
            try:
                existe = InformacionUsuario.objects.get(user = user)
                form2 = InformacionUsuarioForm(request.POST, instance=existe)
            except:
                form2 = InformacionUsuarioForm(request.POST)
            if form.is_valid() & form2.is_valid():
                rolEncUnidad = Group.objects.get(name = 'Encargado de unidad')
                if str(rolEncUnidad.id) in post_values.getlist('groups'):
                    unidades = form2.cleaned_data.get('unidad')
                    if not unidades:
                        return render(request, 'home/Director/editar_usuarios.html', {
                            'segment': 'Lista_Usuarios_Director',
                            'form': form,
                            'form2': form2,
                            'msg': 'Si seleccionas encargado de unidad debes seleccionar la unidad tambien',
                            'msgType': 'warning'
                        })
                form.save()
                exito = form2.save(commit=False)
                exito.user = user
                exito.save()
                return render(request, 'home/Director/editar_usuarios.html', {
                    'segment': 'Lista_Usuarios_Director',
                    'form': form,
                    'form2': form2,
                    'msg': 'Se ha guardado con exito',
                    'msgType': 'success'
                })
            else:
                return render(request, 'home/Director/editar_usuarios.html', {
                    'segment': 'Lista_Usuarios_Director',
                    'form': form,
                    'form2': form2,
                    'msg': 'No se ha podido guardar con exito',
                    'msgType': 'danger'
                })
        else:
            form = GroupAssignForm(request.POST, instance=user)
            try:
                existe = InformacionUsuario.objects.get(user = user)
                form2 = InformacionUsuarioForm(request.POST, instance=existe)
            except:
                form2 = InformacionUsuarioForm(request.POST)
            if form.is_valid() & form2.is_valid():
                rolEncUnidad = Group.objects.get(name = 'Encargado de unidad')
                if str(rolEncUnidad.id) in request.POST.getlist('groups'):
                    unidades = form2.cleaned_data.get('unidad')
                    if not unidades:
                        return render(request, 'home/Director/editar_usuarios.html', {
                            'segment': 'Lista_Usuarios_Director',
                            'form': form,
                            'form2': form2,
                            'msg': 'Si seleccionas encargado de unidad debes seleccionar la unidad tambien',
                            'msgType': 'warning'
                        })
                form.save()
                exito = form2.save(commit=False)
                exito.user = user
                exito.save()
            else:
                return render(request, 'home/Director/editar_usuarios.html', {
                    'segment': 'Lista_Usuarios_Director',
                    'form': form,
                    'form2': form2,
                    'msg': 'No se ha podido guardar con exito',
                    'msgType': 'danger'
                })
            group_ids = list(user.groups.all().values_list('id', flat=True))
            initial = {'groups': group_ids}
            # form = GroupAssignForm(initial=initial, instance=user)
            form.fields['groups'].choices=[(group.id, group.name) for group in Group.objects.all().exclude(name = 'Director')]
            # form2.fields['unidad'].queryset = Unidad.objects.filter(localidad__municipio__jurisdiccion=user.InformacionUsuario.jurisdiccion).order_by('claveclues')
            return render(request, 'home/Director/editar_usuarios.html', {
                'segment': 'Lista_Usuarios_Director',
                'form': form,
                'form2': form2,
                'msg': 'Se ha guardado con exito',
                'msgType': 'success'
            })
    else:
        group_ids = list(user.groups.all().values_list('id', flat=True))
        initial = {'groups': group_ids}
        form = GroupAssignForm(initial=initial, instance=user)
        try:
            existe = InformacionUsuario.objects.get(user = user)
            form2 = InformacionUsuarioForm(instance=existe)
        except:
            form2 = InformacionUsuarioForm()
        if user != request.user:
            form.fields['groups'].choices=[(group.id, group.name) for group in Group.objects.all().exclude(name = 'Director')]
        # form2.fields['unidad'].queryset = Unidad.objects.filter(localidad__municipio__jurisdiccion=user.informacionusuario.jurisdiccion).order_by('claveclues')
        return render(request, 'home/Director/editar_usuarios.html', {
            'segment': 'Lista_Usuarios_Director',
            'form': form,
            'form2': form2
            })
        
        
@login_required(login_url="/login/")
def consultar_unidades(request):
    if request.is_ajax():
        jurisdiccion = request.GET['jurisdiccion_id']
        if jurisdiccion:
            try:
                unidades = Unidad.objects.filter(localidad__municipio__jurisdiccion_id=jurisdiccion).order_by('claveclues')
                # data = [{'id': unidad.id, 'nombre': unidad.nombre, 'claveclues': unidad.claveclues} for unidad in unidades]
                # return JsonResponse({'unidades': data})
                unidades_list = list(unidades.values('pk', 'claveclues'))
                return JsonResponse(unidades_list, safe=False)
            except Exception as e:
                print(e)
                
    return redirect('home')

@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def addMunicipio(request):
    if request.method == 'POST':
        form = MunicipioForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse('vista_tablas', kwargs={'msg':'exitoAddedMunicipio'}))
            except Exception as e:
                return redirect(reverse('vista_tablas', kwargs={'msg':'errorAddedMunicipio'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
    
@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def editMunicipio(request, pk):
    if request.method == 'POST':
        try:
            entity = Municipio.objects.get(id = pk)
        except Exception as e:
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorExistMunicipio'}))
        form = MunicipioForm(request.POST, instance=entity)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse('vista_tablas', kwargs={'msg':'exitoAditedMunicipio'}))
            except Exception as e:
                return redirect(reverse('vista_tablas', kwargs={'msg':'errorAditedMunicipio'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
    
@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def delMunicipio(request, pk):
    if request.method == 'POST':
        try:
            entity = Municipio.objects.get(id = pk)
        except Exception as e:
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorExistMunicipio'}))
        try:
            entity.delete()
            return redirect(reverse('vista_tablas', kwargs={'msg':'exitoDeletedMunicipio'}))
        except Exception as e:
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorDeletedMunicipio'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))