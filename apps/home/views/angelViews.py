from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from apps.home.models import *
from apps.home.forms.allForms import *
from formtools.wizard.views import *

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
