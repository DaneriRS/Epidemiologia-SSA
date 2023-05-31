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
            claveAct = request.POST['clave']
            if Municipio.objects.filter(clave=claveAct).exists():
                return redirect(reverse('vista_tablas', kwargs={'msg':'uniqueAddedMunicipio'}))
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
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorAditedMunicipio'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
    
@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def delMunicipio(request, pk):
    try:
        entity = Municipio.objects.get(id = pk)
    except Exception as e:
        return redirect(reverse('vista_tablas', kwargs={'msg':'errorExistMunicipio'}))
    try:
        entity.delete()
        return redirect(reverse('vista_tablas', kwargs={'msg':'exitoDeletedMunicipio'}))
    except Exception as e:
        return redirect(reverse('vista_tablas', kwargs={'msg':'errorDeletedMunicipio'}))
    
    
@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def addLocalidad(request):
    if request.method == 'POST':
        form = LocalidadForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse('vista_tablas', kwargs={'msg':'exitoAddedLocalidad'}))
            except Exception as e:
                return redirect(reverse('vista_tablas', kwargs={'msg':'errorAddedLocalidad'}))
        else:
            # claveAct = request.POST['clave']
            # if Localidad.objects.filter(clave=claveAct).exists():
            #     return redirect(reverse('vista_tablas', kwargs={'msg':'uniqueAddedLocalidad'}))
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorAddedLocalidad'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
    
@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def editLocalidad(request, pk):
    if request.method == 'POST':
        try:
            entity = Localidad.objects.get(id = pk)
        except Exception as e:
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorExistLocalidad'}))
        form = LocalidadForm(request.POST, instance=entity)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse('vista_tablas', kwargs={'msg':'exitoAditedLocalidad'}))
            except Exception as e:
                return redirect(reverse('vista_tablas', kwargs={'msg':'errorAditedLocalidad'}))
        else:
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorAditedLocalidad'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
    
@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def delLocalidad(request, pk):
    try:
        entity = Localidad.objects.get(id = pk)
    except Exception as e:
        return redirect(reverse('vista_tablas', kwargs={'msg':'errorExistLocalidad'}))
    try:
        entity.delete()
        return redirect(reverse('vista_tablas', kwargs={'msg':'exitoDeletedLocalidad'}))
    except Exception as e:
        return redirect(reverse('vista_tablas', kwargs={'msg':'errorDeletedLocalidad'}))
    
    
@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def addTipologia(request):
    if request.method == 'POST':
        form = TipologiaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse('vista_tablas', kwargs={'msg':'exitoAddedTipologia'}))
            except Exception as e:
                return redirect(reverse('vista_tablas', kwargs={'msg':'errorAddedTipologia'}))
        else:
            claveAct = request.POST['clave']
            if Tipologia.objects.filter(clave=claveAct).exists():
                return redirect(reverse('vista_tablas', kwargs={'msg':'uniqueAddedTipologia'}))
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorAddedTipologia'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
    
@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def editTipologia(request, pk):
    if request.method == 'POST':
        try:
            entity = Tipologia.objects.get(id = pk)
        except Exception as e:
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorExistTipologia'}))
        form = TipologiaForm(request.POST, instance=entity)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse('vista_tablas', kwargs={'msg':'exitoAditedTipologia'}))
            except Exception as e:
                return redirect(reverse('vista_tablas', kwargs={'msg':'errorAditedTipologia'}))
        else:
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorAditedTipologia'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
    
@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def delTipologia(request, pk):
    try:
        entity = Tipologia.objects.get(id = pk)
    except Exception as e:
        return redirect(reverse('vista_tablas', kwargs={'msg':'errorExistTipologia'}))
    try:
        entity.delete()
        return redirect(reverse('vista_tablas', kwargs={'msg':'exitoDeletedTipologia'}))
    except Exception as e:
        return redirect(reverse('vista_tablas', kwargs={'msg':'errorDeletedTipologia'}))


@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def addjurisdiccion(request):
    if request.method == 'POST':
        form = JurisdiccionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse('vista_tablas', kwargs={'msg':'exitoAddedJurisdiccion'}))
            except Exception as e:
                return redirect(reverse('vista_tablas', kwargs={'msg':'errorAddedJurisdiccion'}))
        else:
            claveAct = request.POST['clave']
            if Jurisdiccion.objects.filter(clave=claveAct).exists():
                return redirect(reverse('vista_tablas', kwargs={'msg':'uniqueAddedJurisdiccion'}))
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorAddedJurisdiccion'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
    
@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def editjurisdiccion(request, pk):
    if request.method == 'POST':
        try:
            entity = Jurisdiccion.objects.get(id = pk)
        except Exception as e:
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorExistJurisdiccion'}))
        form = JurisdiccionForm(request.POST, instance=entity)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse('vista_tablas', kwargs={'msg':'exitoAditedJurisdiccion'}))
            except Exception as e:
                return redirect(reverse('vista_tablas', kwargs={'msg':'errorAditedJurisdiccion'}))
        else:
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorAditedJurisdiccion'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
    
@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def deljurisdiccion(request, pk):
    try:
        entity = Jurisdiccion.objects.get(id = pk)
    except Exception as e:
        return redirect(reverse('vista_tablas', kwargs={'msg':'errorExistJurisdiccion'}))
    try:
        entity.delete()
        return redirect(reverse('vista_tablas', kwargs={'msg':'exitoDeletedJurisdiccion'}))
    except Exception as e:
        return redirect(reverse('vista_tablas', kwargs={'msg':'errorDeletedJurisdiccion'}))

@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def addInstitucion(request):
    if request.method == 'POST':
        form = InstitucionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse('vista_tablas', kwargs={'msg':'exitoAddedInstitucion'}))
            except Exception as e:
                return redirect(reverse('vista_tablas', kwargs={'msg':'errorAddedInstitucion'}))
        else:
            claveAct = request.POST['clave']
            if Institucion.objects.filter(clave=claveAct).exists():
                return redirect(reverse('vista_tablas', kwargs={'msg':'uniqueAddedInstitucion'}))
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorAddedInstitucion'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
    
@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def editInstitucion(request, pk):
    if request.method == 'POST':
        try:
            entity = Institucion.objects.get(id = pk)
        except Exception as e:
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorExistInstitucion'}))
        form = InstitucionForm(request.POST, instance=entity)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse('vista_tablas', kwargs={'msg':'exitoAditedInstitucion'}))
            except Exception as e:
                return redirect(reverse('vista_tablas', kwargs={'msg':'errorAditedInstitucion'}))
        else:
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorAditedInstitucion'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
    
@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def delInstitucion(request, pk):
    try:
        entity = Institucion.objects.get(id = pk)
    except Exception as e:
        return redirect(reverse('vista_tablas', kwargs={'msg':'errorExistInstitucion'}))
    try:
        entity.delete()
        return redirect(reverse('vista_tablas', kwargs={'msg':'exitoDeletedInstitucion'}))
    except Exception as e:
        return redirect(reverse('vista_tablas', kwargs={'msg':'errorDeletedInstitucion'}))
    
    
@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def addUnidad(request):
    if request.method == 'POST':
        form = UnidadForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse('vista_tablas', kwargs={'msg':'exitoAddedUnidad'}))
            except Exception as e:
                return redirect(reverse('vista_tablas', kwargs={'msg':'errorAddedUnidad'}))
        else:
            claveAct = request.POST['clave']
            if Unidad.objects.filter(clave=claveAct).exists():
                return redirect(reverse('vista_tablas', kwargs={'msg':'uniqueAddedUnidad'}))
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorAddedUnidad'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
    
@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def editUnidad(request, pk):
    if request.method == 'POST':
        try:
            entity = Unidad.objects.get(id = pk)
        except Exception as e:
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorExistUnidad'}))
        form = UnidadForm(request.POST, instance=entity)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse('vista_tablas', kwargs={'msg':'exitoAditedUnidad'}))
            except Exception as e:
                return redirect(reverse('vista_tablas', kwargs={'msg':'errorAditedUnidad'}))
        else:
            return redirect(reverse('vista_tablas', kwargs={'msg':'errorAditedUnidad'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
    
@login_required(login_url="/login/")
@roles_required(['Director'], redirect_url='home')
def delUnidad(request, pk):
    try:
        entity = Unidad.objects.get(id = pk)
    except Exception as e:
        return redirect(reverse('vista_tablas', kwargs={'msg':'errorExistUnidad'}))
    try:
        entity.delete()
        return redirect(reverse('vista_tablas', kwargs={'msg':'exitoDeletedUnidad'}))
    except Exception as e:
        return redirect(reverse('vista_tablas', kwargs={'msg':'errorDeletedUnidad'}))
    
@login_required(login_url="/login/")
def TodosLosReportes(request, msg):
    if request.user.is_director:
        Registro = RegistroEstudio.objects.all()
        NotifBrote = NotificacionBrote.objects.all()
        Anexo = Anexo8.objects.all()
    elif request.user.is_encarJuris:
        Registro = RegistroEstudio.objects.filter(unidadNot__jurisdiccion__id=request.user.informacionusuario.unidad.jurisdiccion.id)
        NotifBrote = NotificacionBrote.objects.filter(unidadNot__jurisdiccion__id=request.user.informacionusuario.unidad.jurisdiccion.id)
        Anexo = Anexo8.objects.filter(capturante__informacionusuario__jurisdiccion__id=request.user.informacionusuario.jurisdiccion.id)
    elif request.user.is_encarUni:
        Registro = RegistroEstudio.objects.filter(unidadNot__id=request.user.informacionusuario.unidad.id)
        NotifBrote = NotificacionBrote.objects.filter(unidadNot__id=request.user.informacionusuario.unidad.id)
        Anexo = Anexo8.objects.filter(capturante__informacionusuario__unidad__id=request.user.informacionusuario.unidad.id)
     
    return render(request, 'home/TodosLosReportes.html', {
        'segment': 'Reportes',
        'Registro': Registro,
        'NotifBrote': NotifBrote,
        'Anexo': Anexo,
    })