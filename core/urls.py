# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import urls
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path  # add this
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    # ADD NEW Routes HERE
    #path(r'^media/', include('media.logos.urls', 'logos')),
    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#urlpatterns += [
      #  re_path(r'^media/(?P<path>.*)$', serve, {
     #   'document_root': settings.MEDIA_ROOT,
    #})]
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)