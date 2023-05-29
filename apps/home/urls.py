# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from apps.home.views import allViews

urlpatterns = [

    # The home page
    path('', allViews.index, name='home'),
    path('import_excel/', allViews.import_excel, name='import_excel_view'),
    # path('listaFormularios/', allViews.listaFormularios , name="listaFormularios"),
    # path('listaNotificacionBrote/', allViews.listaNotificacionBrote , name="listaNotificacionBrote"),
    # path('listaAnexo8/', allViews.listaAnexo8 , name="listaAnexo8"),
    path('nuevoPaciente/', allViews.nuevoPaciente, name="nuevoPaciente"),
    path('usuarios/', allViews.lista_usuarios, name="lista_usuarios"),
    path('usuarios/editar/<int:user_id>/', allViews.editar_usuarios, name='editarUsuarios'),
    path('ajax/consultar/unidades/', allViews.consultar_unidades, name='get_unidades'),
    path('perfil/<int:user_id>', allViews.user, name='user'),
    

    path('tablas/<str:msg>/', allViews.vista_tablas, name='vista_tablas'),
    path('tabla/<str:msg>/', allViews.vista_logos, name='vista_logos'),
    #path('logos/<str:msg>/', allViews.vista_logos, name='vista_logos'),
    path('perfil/', allViews.user, name='user'),

    # Matches any html file
    # No borrar esta URL
    # re_path(r'^.*\.*', allViews.pages, name='pages'),

    #CRUD INSTITUCION
    path('tablas/institucion/add', allViews.addInstitucion, name = 'addInstitucion'),
    path('tablas/institucion/del/<int:pk>', allViews.delInstitucion, name = 'delInstitucion'),
    path('tablas/institucion/edit/<int:pk>', allViews.editInstitucion, name = 'editInstitucion'),
    
    #CRUD MUNICIPIO
    path('tablas/municipio/add', allViews.addMunicipio, name = 'addMunicipio'),
    path('tablas/municipio/del/<int:pk>', allViews.delMunicipio, name = 'delMunicipio'),
    path('tablas/municipio/edit/<int:pk>', allViews.editMunicipio, name = 'editMunicipio'),
    
    #CRUD JURISDICCION
    path('tablas/jurisdiccion/add', allViews.addjurisdiccion, name = 'addjurisdiccion'),
    path('tablas/jurisdiccion/del/<int:pk>', allViews.deljurisdiccion, name = 'deljurisdiccion'),
    path('tablas/jurisdiccion/edit/<int:pk>', allViews.editjurisdiccion, name = 'editjurisdiccion'),
    
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
    path('tablas/Entidad/edit/<int:pk>', allViews.editEntidad, name = 'editEntidad'),
    path('tablas/Entidad/del/<int:pk>', allViews.delEntidad, name = 'delEntidad'),

    #CRUD ESTABLECIMIENTO
    path('tablas/Establecimiento/add', allViews.addEstablecimiento, name = 'addEstablecimiento'),
    path('tablas/Establecimiento/edit/<int:pk>', allViews.editEstablecimiento, name = 'editEstablecimiento'),
    path('tablas/Establecimiento/del/<int:pk>', allViews.delEstablecimiento, name = 'delEstablecimiento'),
    
    #CRUD ESTABLECIMIENTO
    path('tablas/Unidad/add', allViews.addUnidad, name = 'addUnidad'),
    path('tablas/Unidad/edit/<int:pk>', allViews.editUnidad, name = 'editUnidad'),
    path('tablas/Unidad/del/<int:pk>', allViews.delUnidad, name = 'delUnidad'),

    #LocalidadExcel
    path('tablas/localidad/Excel/', allViews.LocalidadExcel, name = 'LocalidadExcel'),

    #MunicpioExcel
    path('tablas/municipio/Excel/', allViews.MunicipioExcel, name = 'MunicipioExcel'),

    #UnidadMedicaExcel
    path('tablas/umedica/Excel/', allViews.UMedicaExcel, name = 'UMedicaExcel'),

    #Logos
    path('Logos/', allViews.actualizarLogos, name = 'actualizarLogos'),
    path('listaLogos/', allViews.ListaLogos, name = 'listaLogos'),
    path('tabla/Logos/edit/<int:pk>', allViews.editLogo, name = 'editLogo'),
    path('tablas/Logos/del/<int:pk>', allViews.delLogo, name = 'delLogo'),

    #FormWizardViews
    path('Reporte/Registro/Create/', allViews.RegistroEstudioView.as_view() , name="multiForm"),
    path('Reporte/Registro/Update/<int:id>/', allViews.RegistroEstudioUpdateView.as_view() , name="editForm"),
    path('Reporte/NotificacionBrote/Create/', allViews.RegistroNotificacionBroteView.as_view() , name="notificacionBrote"),
    path('Reporte/NotificacionBrote/Update/<int:id>/', allViews.UpdateNotificacionBroteView.as_view() , name="notificacionBroteUpdate"),
    path('Reporte/Anexo8/Create/', allViews.Anexo8View.as_view() , name="anexo8"),
    # path('Reporte/Anexo8/Create/', lambda request: allViews.Anexo8View.as_view(segment='Reportes')(request), name="anexo8"),
    path('Reporte/Anexo8/Create/<int:id>/', allViews.UpdateAnexo8View.as_view() , name="anexo8Update"),

    #Reportes
    path('Reporte/Registro/Export/', allViews.ReporteRegExcel, name = 'reporteRegExcel'),
    path('Reporte/NotificacionBrote/Export/', allViews.ReporteNotiExcel, name = 'reporteNotiExcel'),
    path('Reporte/Anexo8/Export/', allViews.ReporteAnexoExcel, name = 'reporteAnexoExcel'),
    
    #Punto Partida Reportes
    path('Reportes/All/<str:msg>/', allViews.TodosLosReportes, name = 'TodosLosReportes'),

]

