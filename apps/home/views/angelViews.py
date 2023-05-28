from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from apps.home.models import *
from apps.home.forms.allForms import *
from formtools.wizard.views import *
from django.contrib.auth.decorators import user_passes_test
from django.forms.models import model_to_dict

def roles_required(roles, redirect_url=None):
    def decorator(view_func):
        @user_passes_test(lambda user: user.groups.filter(name__in=roles).exists(), login_url=redirect_url)
        def wrapper(request, *args, **kwargs):
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

FormSET1=formset_factory(ContactoForm4, extra=2)
FormSET12=formset_factory(ContactoForm7, extra=2)
FORMS = [
            ("1", ContactForm1),
            ("2", ContactForm2),
            ("3", ContactForm3),
            ("4", FormSET1),
            ("5", ContactoForm6),
            ("6", FormSET12),
            ("7", ContactoForm8),
            ("8", ContactoForm9),
            ("9", ContactoForm10),
            ("10", ContactoForm11),
        ]
FormSET2=formset_factory(ContactoForm5, extra=0)
FORMS2 = [
            ("1", ContactForm1),
            ("2", ContactForm2),
            ("3", ContactForm3),
            ("4", FormSET2)
        ]
FormSET3=formset_factory(NotificacionBrote5, extra=1)
FORMS3 =[
            ("1", NotificacionBrote1),
            ("2", NotificacionBrote2),
            ("3", FormSET3),
            ("4", NotificacionBrote6),
            ("5", NotificacionBrote7)
        ]
FormSET4=formset_factory(NotificacionBrote8, extra=0)
FORMS4 =[
            ("1", NotificacionBrote1),
            ("2", NotificacionBrote2),
            ("3", FormSET4),
            ("4", NotificacionBrote6),
            ("5", NotificacionBrote7)
        ]
FORMS5 =[
    ('1', Anexo8P1),
    ('2', Anexo8P2),
    ('3', Anexo8P3),
    ('4', Anexo8P4)
]
FORMS6 =[
    ('1', Anexo8P1),
    ('2', Anexo8P2),
    ('3', Anexo8P3),
    ('4', Anexo8P4)
]

class RegistroEstudioView(CookieWizardView):
    form_list=FORMS
    form_dict=dict(form_list)
    template_name = 'home/exampleForm.html'

    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)
        
    def get_form_initial(self, step):
        step = step or self.steps.current
        initial = self.initial_dict.get(step, {})
        if step == '1':
            # Set initial data for step 2 form here
            initial['unidadNot'] = self.request.user.informacionusuario.unidad
            
        return initial

    def done(self, form_list, **kwargs):
        registroDataFormSet1=[]
        registroDataFormSet12=[]
        registroData={}
        for i,form in enumerate(form_list):
            if i != 3 and i != 5:
                registroData.update(form.cleaned_data)
            elif i == 3:
                for formset in form:
                    registroDataFormSet1.append(formset.cleaned_data)
            elif i==5:
                for formset in form:
                    registroDataFormSet12.append(formset.cleaned_data)
            
        rd = RegistroEstudio(**registroData)
        rd.save()

        for item in registroDataFormSet1:
            est=Estudio(
                nombre=item['nombre'],
                tipo=item['tipo'],
                fecha=item['fecha'],
                resultado=item['resultado'],
                registroEstudio=rd
            )
            est.save()

        for item in registroDataFormSet12:
            cont=Contacto(
                nombre=item['nombre'],
                domicilio=item['domicilio'],
                edad=item['edad'],
                sexo=item['sexo'],
                contacto=item['contacto'],
                caso=item['caso']
            )
            cont.save()
        return redirect('listaFormularios')

class RegistroEstudioUpdateView(CookieWizardView):
    form_list=FORMS2
    form_dict=dict(form_list)
    template_name = 'home/editForm1.html'
    

    def get_form_initial(self, step):
        step = step or self.steps.current
        if 'id' in self.kwargs:
            project_id = self.kwargs['id']
            project = RegistroEstudio.objects.get(id=project_id)
            if step == "4":
                project_dict=[]
                estudios=Estudio.objects.filter(registroEstudio_id=project.id)
                for estudio in estudios:
                    project_d = model_to_dict(estudio)
                    project_dict.append(project_d)
                return project_dict
            else:
                project_dict = model_to_dict(project)
                return project_dict

    def done(self, form_list, **kwargs):
        id = self.kwargs['id']

        registroDataFormSet1=[]
        registroData={}

        for i,form in enumerate(form_list):
            if i != 3:
                registroData.update(form.cleaned_data)
            else:
                for formset in form:
                    registroDataFormSet1.append(formset.cleaned_data)

        re=RegistroEstudio.objects.filter(id=id)
        re.update(**registroData)

        for item in registroDataFormSet1:
            est=Estudio.objects.get(id=item['id'])
            est.nombre=item['nombre']
            est.tipo=item['tipo']
            est.fecha=item['fecha']
            est.resultado=item['resultado']
            est.save()

        return redirect('listaFormularios')

class RegistroNotificacionBroteView(CookieWizardView):
    form_list=FORMS3
    form_dict=dict(form_list)
    template_name = 'home/notificacionBrote.html'

    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        registroDataFormSet3=[]
        registroData={}
        for i,form in enumerate(form_list):
            if i != 2:
                registroData.update(form.cleaned_data)
            elif i == 2:
                for formset in form:
                    registroDataFormSet3.append(formset.cleaned_data)

        notificacion=NotificacionBrote(**registroData)
        notificacion.save()

        for item in registroDataFormSet3:
            DistGeo=DistribucionGeografica(
                area=item['area'],
                numeroCasos=item['numeroCasos'],
                numeroDefunciones=item['numeroDefunciones'],
                notificacionBrote=notificacion
            )
            DistGeo.save()

        return redirect('listaNotificacionBrote')    

class UpdateNotificacionBroteView(CookieWizardView):
    form_list=FORMS4
    form_dict=dict(form_list)
    template_name = 'home/editarNotBrote.html'

    def get_form_initial(self, step):
        step = step or self.steps.current
        if 'id' in self.kwargs:
            project_id = self.kwargs['id']
            project = NotificacionBrote.objects.get(id=project_id)
            if step == "3":
                project_dict=[]
                distGeo=DistribucionGeografica.objects.filter(notificacionBrote_id=project.id)
                for dist in distGeo:
                    project_d = model_to_dict(dist)
                    project_dict.append(project_d)
                return project_dict
            else:
                project_dict = model_to_dict(project)
                return project_dict

    def done(self, form_list, **kwargs):
        id = self.kwargs['id']

        registroDataFormSet4=[]
        registroData={}

        for i,form in enumerate(form_list):
            if i != 2:
                registroData.update(form.cleaned_data)
            elif i == 2:
                for formset in form:
                    registroDataFormSet4.append(formset.cleaned_data)

        notificacion=NotificacionBrote.objects.filter(id=id)
        notificacion.update(**registroData)

        for item in registroDataFormSet4:
            dist=DistribucionGeografica.objects.get(id=item['id'])
            dist.area=item['area']
            dist.numeroCasos=item['numeroCasos']
            dist.numeroDefunciones=item['numeroDefunciones']
                                           
            dist.save()

        return redirect('listaNotificacionBrote')

class Anexo8View(CookieWizardView):
    form_list = FORMS5
    form_dict = dict(form_list)
    template_name = 'home/anexo8.html'

    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)
        
    def done(self, form_list, **kwargs):
        registroData={}
        for i,form in enumerate(form_list):
            registroData.update(form.cleaned_data)

        anexo8=Anexo8(**registroData)
        anexo8.save()

        return redirect('listaAnexo8')

class UpdateAnexo8View(CookieWizardView):
    form_list = FORMS6
    form_dict = dict(form_list)
    template_name = 'home/editarAnexo8.html'

    def get_form_initial(self, step):
        step = step or self.steps.current
        if 'id' in self.kwargs:
            project_id = self.kwargs['id']
            project = Anexo8.objects.get(id=project_id)
            project_dict = model_to_dict(project)
            return project_dict
        
    def done(self, form_list, **kwargs):
        id = self.kwargs['id']

        registroData={}
        for i,form in enumerate(form_list):
            registroData.update(form.cleaned_data)

        anexo8=Anexo8.objects.filter(id=id)
        anexo8.update(**registroData)

        return redirect('listaAnexo8')

@login_required    
def listaFormularios(request):
    if request.method == 'GET':
        formularios = RegistroEstudio.objects.all()
        return render(request, 'home/tablaForms.html', {'formularios': formularios})
    else:
        return redirect ('home')
    
@login_required
def listaNotificacionBrote(request):
    if request.method == 'GET':
        formularios = NotificacionBrote.objects.all()
        return render(request, 'home/ListaNotificacionBrotes.html', {'formularios': formularios})
    else:
        return redirect ('home')

@login_required
def listaAnexo8(request):
    if request.method == 'GET':
        formularios = Anexo8.objects.all()
        return render(request, 'home/ListaAnexo8.html', {'formularios': formularios})
    else:
        return redirect ('home')

def nuevoPaciente(request):
    msg=''
    msgType=''
    if request.method == 'POST':
        formA = registroPaciente(request.POST)
        form = registroPaciente()
        print(request.POST.get('numAfiliacion'))
        if formA.is_valid():
            
            try:
                formA.save()
                msg='Paciente Registrado con Exito'
                msgType='success'
                return render(request, 'home/nuevoPaciente.html', {
                    'form': form,
                    'msg' : msg,
                    'msgType' : msgType
                })
            except:
                msg='Error al registrar al paciente'
                msgType='danger'
                return render(request, 'home/nuevoPaciente.html', {
                    'form': form,
                    'msg' : msg,
                    'msgType' : msgType
                })
        else:
            paciente_exist= Paciente.objects.filter(numAfiliacion=request.POST.get('numAfiliacion')).exists()
            if paciente_exist:
                msg='Ya existe el paciente con el numero de afiliacion: '+request.POST.get('numAfiliacion')
                msgType='danger'
            else:
                msg='Error al registrar al paciente'
                msgType='danger'

            return render(request, 'home/nuevoPaciente.html', {
                'form': form,
                'msg' : msg,
                'msgType' : msgType
            })
    else:
        form = registroPaciente()
    
    return render(request, 'home/nuevoPaciente.html', {'form': form})
