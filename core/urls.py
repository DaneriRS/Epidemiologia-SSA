# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import statistics
from django import urls
from django.conf import settings
from django.contrib import admin
from django.urls import path, include  # add this
from django.conf.urls. static import static

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    # ADD NEW Routes HEREdocument_root': settings.MEDIA_ROOT}),
    #path(r'^logotipos/', include('logotipos.urls')),

    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)