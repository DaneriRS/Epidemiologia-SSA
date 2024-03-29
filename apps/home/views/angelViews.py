from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from apps.home.models import *
from apps.home.forms.allForms import *
from formtools.wizard.views import *
from django.contrib.auth.decorators import user_passes_test

def roles_required(roles, redirect_url=None):
    def decorator(view_func):
        @user_passes_test(lambda user: user.groups.filter(name__in=roles).exists(), login_url=redirect_url)
        def wrapper(request, *args, **kwargs):
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

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

    #CRUD JURISDICCION

    #CRUD INSTITUCION
def addInstitucionCrud(request):
    formAddJurisdiccion = addJurisdiccion()
    formAddInstitucion = addInstitucion()
    if request.method == 'POST':
        form = addInstitucion(request.POST)
        if form.is_valid():
            try:
                form.save()
                # mensaje = None
                # msgType = None
                # mensaje = 'Mensaje 1 de prueba'
                # msgType = 'success'
                # context = {
                #     'segment': 'CRUD_tablas',
                #     'mensaje':mensaje,
                #     'msg': mensaje,
                #     'msgType': msgType,
                #     'formAddJurisdiccion' : formAddJurisdiccion,
                #     'formAddInstitucion' : formAddInstitucion
                # }
                # return render(request, 'home/Director/CRUDTablas.html', context)
                return redirect(reverse('vista_tablas', kwargs={'msg':'Exito create insti'}))
            except:
                print('error')
                

def delInstitucion(request, pk):
    formAddJurisdiccion = addJurisdiccion()
    formAddInstitucion = addInstitucion()

    try:
        insti = Institucion.objects.get(id=pk)
        insti.delete()
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
        'formAddJurisdiccion' : formAddJurisdiccion,
        'formAddInstitucion' : formAddInstitucion
    }
    return render(request, 'home/Director/CRUDTablas.html', context)

