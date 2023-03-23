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

    # Matches any html file
    # No borrar esta URL
    # re_path(r'^.*\.*', allViews.pages, name='pages'),

    #CRUD INSTITUCION
    path('tablas/jurisdiccion/add', allViews.addInstitucionCrud, name = 'addInstitucionCrud'),
    path('tablas/jurisdiccion/del/<pk>', allViews.delInstitucion, name = 'delInstitucion'),

    

]
