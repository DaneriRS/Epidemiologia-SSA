from django.contrib.auth.decorators import login_required
from django.urls import reverse
import pandas as pd
from django.shortcuts import redirect, render
from apps.home.models import *
from apps.home.forms.allForms import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import user_passes_test

def roles_required(roles, redirect_url=None):
    def decorator(view_func):
        @user_passes_test(lambda user: user.groups.filter(name__in=roles).exists(), login_url=redirect_url)
        def wrapper(request, *args, **kwargs):
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

@login_required
def import_excel(request):
    form=ExcelForm()
    form2=IndividualForm()
    if request.method == 'POST' and "Excel" in request.POST:
        excel_file = request.FILES['Subir_Excel']
        df = pd.read_excel(excel_file)

        try:
            # Itera a través de cada fila del DataFrame
            for index, row in df.iterrows():
                # Crea una instancia del modelo con los datos de la fila
                obj = User(
                    username=row['username'],
                    first_name=row['nombre'],
                    last_name=row['apellidos'],
                    email=row['correo'],
                    password=make_password(row['password']),
                    # Continúa agregando todos los campos del modelo que quieras importar
                )
                # Guarda la instancia del modelo en la base de datos
                obj.save()
            print('todo bien')
            return render(request, 'home/registrar_excel.html',{
                'form': form,
                'form2': form2
            })
        except:
            print('error')
            return render(request, 'home/registrar_excel.html',{
                'form': form,
                'form2': form2
            })
    if request.method == 'POST' and "Individual" in request.POST:
        obj = User(
            username=request.POST['Usuario'],
            first_name=request.POST['Nombre'],
            last_name=request.POST['Apellidos'],
            email=request.POST['Correo'],
            password=make_password(request.POST['Contraseña']),
        )
        obj.save()
        return render(request, 'home/registrar_excel.html',{
            'form': form,
            'form2': form2
        })
    else:
        return render(request, 'home/registrar_excel.html',{
            'form': form,
            'form2': form2
        })

@login_required
@roles_required(['Director'], redirect_url='home')
def LocalidadExcel(request):
    if request.method=="POST" and "ExcelLocalidad" in request.POST:
        print("localidad")
        excel_file = request.FILES['Subir_LocalidadExcel']
        df = pd.read_excel(excel_file)

        try:
            # Itera a través de cada fila del DataFrame
            for index, row in df.iterrows():
                # Crea una instancia del modelo con los datos de la fila
                print(str(row['clave']) + " - " +str(row['nombre']))
                obj = Localidad(
                    clave=row['clave'],
                    nombre=row['nombre'],
                    # Continúa agregando todos los campos del modelo que quieras importar
                )
                # # Guarda la instancia del modelo en la base de datos
                obj.save()
            return redirect(reverse('vista_tablas', kwargs={'msg':'Exito Registro Excel'}))
        except:
            print('error')
            return redirect(reverse('vista_tablas', kwargs={'msg':'Error Registro Excel'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
    

@login_required
@roles_required(['Director'], redirect_url='home')
def MunicipioExcel(request):
    if request.method=="POST" and "ExcelMunicipio" in request.POST:
        print("municipio")
        excel_file = request.FILES['Subir_MunicipioExcel']
        df = pd.read_excel(excel_file)

        try:
            # Itera a través de cada fila del DataFrame
            print(df)
            for index, row in df.iterrows():
                print(str(row['clave']) + " - " +str(row['nombre'])+ " - " +str(row['entidad']))
                entidad=Entidad.objects.get(clave=row['entidad'])
                # Crea una instancia del modelo con los datos de la fila
                obj = Municipio(
                    clave=row['clave'],
                    nombre=row['nombre'],
                    entidad=entidad,
                    # Continúa agregando todos los campos del modelo que quieras importar
                )
                # # Guarda la instancia del modelo en la base de datos
                obj.save()
            return redirect(reverse('vista_tablas', kwargs={'msg':'Exito Registro Excel'}))
        except Exception as e:
            print('error')
            return redirect(reverse('vista_tablas', kwargs={'msg':'Error Registro Excel'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
 

@login_required
@roles_required(['Director'], redirect_url='home')
def UMedicaExcel(request):
    if request.method=="POST" and "ExcelUMedicas" in request.POST:
        print("Unidad Medica")
        excel_file = request.FILES['Subir_UmedicasExcel']
        df = pd.read_excel(excel_file)

        try:
            # Itera a través de cada fila del DataFrame
            for index, row in df.iterrows():
                tipologia= Tipologia.objects.get(clave=row['tipologia'])
                establecimiento= Establecimiento.objects.get(clave=row['establecimiento'])
                institucion= Institucion.objects.get(clave=row['institucion'])
                localidad= Localidad.objects.get(clave=row['localidad'])
                municipio=Municipio.objects.get(nombre=row['municipio'])
                jurisdiccion=Jurisdiccion.objects.get(clave=row['jurisdiccion'])
                # Crea una instancia del modelo con los datos de la fila
                print(str(row['claveclues']) + " - " +str(row['claveSuave'])+ " - " +str(row['tipologia'])+ " - " +str(row['establecimiento'])+ " - " +str(row['institucion'])+ " - " +str(row['localidad'])+ " - " +str(row['municipio'])+ " - " +str(row['jurisdiccion']))
                obj = Unidad(
                    claveclues=row['claveclues'],
                    claveSuave=row['claveSuave'],
                    tipologia=tipologia,
                    establecimiento=establecimiento,
                    institucion=institucion,
                    localidad=localidad,
                    municipio=municipio,
                    jurisdiccion=jurisdiccion
                    # Continúa agregando todos los campos del modelo que quieras importar
                )
                # #Guarda la instancia del modelo en la base de datos
                obj.save()
            return redirect(reverse('vista_tablas', kwargs={'msg':'Exito Registro Excel'}))
        except:
            print('error')
            return redirect(reverse('vista_tablas', kwargs={'msg':'Error Registro Excel'}))
    else:
        return redirect(reverse('vista_tablas', kwargs={'msg':'false'}))
   


    