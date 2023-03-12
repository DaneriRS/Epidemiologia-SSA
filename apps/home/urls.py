# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('import_excel/', views.import_excel, name='import_excel_view'),
    path('multiForm', views.BookingWizzadView.as_view() , name="multiForm"),
    path('nuevoPaciente', views.nuevoPaciente, name="nuevoPaciente"),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    

]
