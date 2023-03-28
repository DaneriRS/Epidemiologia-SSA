# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home.views import allViews

urlpatterns = [

    # The home page
    path('', allViews.index, name='home'),
    path('import_excel/', allViews.import_excel, name='import_excel_view'),
    path('multiForm/', allViews.BookingWizzadView.as_view() , name="multiForm"),
    path('nuevoPaciente/', allViews.nuevoPaciente, name="nuevoPaciente"),
    path('usuarios/', allViews.lista_usuarios, name="lista_usuarios"),
    path('usuarios/editar/<int:user_id>/', allViews.editar_usuarios, name='editarUsuarios'),
    path('ajax/consultar/unidades/', allViews.consultar_unidades, name='get_unidades'),
    path('tablas/<str:msg>/', allViews.vista_tablas, name='vista_tablas'),
    path('perfil/', allViews.user, name='user'),

    # Matches any html file
    # No borrar esta URL
    # re_path(r'^.*\.*', allViews.pages, name='pages'),

    #CRUD INSTITUCION
    path('tablas/jurisdiccion/add', allViews.addInstitucionCrud, name = 'addInstitucionCrud'),
    path('tablas/jurisdiccion/del/<int:pk>', allViews.delInstitucion, name = 'delInstitucion'),
    
    #CRUD MUNICIPIO
    path('tablas/municipio/add', allViews.addMunicipio, name = 'addMunicipio'),
    path('tablas/municipio/del/<int:pk>', allViews.delMunicipio, name = 'delMunicipio'),
    path('tablas/municipio/edit/<int:pk>', allViews.editMunicipio, name = 'editMunicipio'),
    
    #CRUD LOCALIDAD
    path('tablas/localidad/add', allViews.addLocalidad, name = 'addLocalidad'),
    path('tablas/localidad/del/<int:pk>', allViews.delLocalidad, name = 'delLocalidad'),
    path('tablas/localidad/edit/<int:pk>', allViews.editLocalidad, name = 'editLocalidad'),
    
    #CRUD TIPOLOGIA
    path('tablas/tipologia/add', allViews.addTipologia, name = 'addTipologia'),
    path('tablas/tipologia/del/<int:pk>', allViews.delTipologia, name = 'delTipologia'),
    path('tablas/tipologia/edit/<int:pk>', allViews.editTipologia, name = 'editTipologia'),

    #CRUD ENTIDAD
    path('tablas/Entidad/add', allViews.addEntidad, name = 'addEntidad'),
    path('tablas/Entidad/edit/<pk>', allViews.editEntidad, name = 'editEntidad'),
    path('tablas/Entidad/del/<pk>', allViews.delEntidad, name = 'delEntidad'),

    #CRUD ESTABLECIMIENTO
    path('tablas/Establecimiento/add', allViews.addEstablecimiento, name = 'addEstablecimiento'),
    path('tablas/Establecimiento/edit/<pk>', allViews.editEstablecimiento, name = 'editEstablecimiento'),
    path('tablas/Establecimiento/del/<pk>', allViews.delEstablecimiento, name = 'delEstablecimiento'),

    #LocalidadExcel
    path('tablas/localidad/Excel/', allViews.LocalidadExcel, name = 'LocalidadExcel'),

    #MunicpioExcel
    path('tablas/municipio/Excel/', allViews.MunicipioExcel, name = 'MunicipioExcel'),

    #UnidadMedicaExcel
    path('tablas/umedica/Excel/', allViews.UMedicaExcel, name = 'UMedicaExcel'),

]
