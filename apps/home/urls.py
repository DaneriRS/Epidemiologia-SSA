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
    path('multiForm', allViews.BookingWizzadView.as_view() , name="multiForm"),
    path('nuevoPaciente', allViews.nuevoPaciente, name="nuevoPaciente"),
    path('usuarios/', allViews.lista_usuarios, name="lista_usuarios"),
    path('usuarios/editar/<int:user_id>/', allViews.assign_groups, name='editarUsuarios'),
    path('perfil', allViews.user, name='user'),
    path('editarPerfil/<int:user_id>', allViews.editU, name='editarPerfil'),
    path('actualizarPerfil/<int:user_id>', allViews.actualizarU, name='actualizarPerfil'),
    
    # Matches any html file
    # No borrar esta URL
    # re_path(r'^.*\.*', allViews.pages, name='pages'),

    

]
