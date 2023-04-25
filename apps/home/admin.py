# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from apps.home.models import *

# Register your models here.

admin.site.register(InformacionUsuario)
admin.site.register(Jurisdiccion)
admin.site.register(Unidad)
admin.site.register(Entidad)
admin.site.register(Logos)

