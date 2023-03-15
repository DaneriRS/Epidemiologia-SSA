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
    path('usuarios/asignar-grupos/<int:user_id>/', allViews.assign_groups, name='assign_groups'),

    # Matches any html file
    re_path(r'^.*\.*', allViews.pages, name='pages'),

    

]
