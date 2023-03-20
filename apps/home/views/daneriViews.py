from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import method_decorator
from django.http import HttpResponseRedirect
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
    if request.method == "POST":
        obj = User(
            username=request.POST['Usuario'],
            first_name=request.POST['Nombre'],
            last_name=request.POST['Apellidos'],
            email=request.POST['Correo'],
            password=request.POST['Contraseña'],
        )
        obj2 = Unidad(
            claveclues = request.POST['Clave'],
            establecimiento = request.POST['Establecimiento'],
            institucion = request.POST['Institucion'],
            localidad = request.POST['Municipio'],

        )
        obj.save()
        obj2.save()
    return render(request, "home/user.html")

class UserView(TemplateView):
    template_name = 'user/list.html'
@method_decorator(csrf_exept)
@method_decorator(login_required)
def dispatch(self, request, *args, **kwargs):
            return super().__init__.dispatch(request, *args, **kwargs)

def post(self, request, *args, **kwargs):
    data = {}
    try:
        data = super().objects.get(pk=request.POST['id']).toJson()
        
    except Exception as e:
        data['error']= str(e)
    return JSONResponse(data)


@login_required(login_url="/login/")
def editU(request, user_id):
    user = User.objects.filter(pk=user_id)
    form = actualizarU(instance=user)
    return render(request,"home/user.html", {'form':form, 'user':user})


@login_required(login_url="/login/")
@permission_required('User.can_edit')
def actualizarU(request, pk):
    #user = User.object.get(pk=user_id)

    perf=get_object_or_404(BookInstance, pk = pk)
    #user = get_object_or_404(BookInstance, pk)

    form = actualizaPerfil(request.POST,isinstance=perf)

    if request.method == 'POST':
        form = actualizaPerfil(request.POST)

        if form.is_valid():
            perf.due_back = form.cleaned_data['']
            perf.save()
                #user = User.objects.all()
            return HttpResponseRedirect(reversed('Datos-eliminados'))

    else:
        form = actualizaPerfil(initial={'username': '','email': '', 'password': '', 'first_name': '', 'last_name'
'unidad': '', 'claveClues': '', 'jurisdiccion': '', 'municipio': '',
'entidad': '', 'groups': ''})
        user = User.objects.all()
    return render(request, "home/user.html", {'form':form, 'bookinst':perf})
