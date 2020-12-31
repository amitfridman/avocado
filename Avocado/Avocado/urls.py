"""Avocado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import settings
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


class SimpleStaticView(TemplateView):
    def get_template_names(self):
        return [self.kwargs.get('template_name') + ".html"]

    def get(self, request, *args, **kwargs):
        return super(SimpleStaticView, self).get(request, *args, **kwargs)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('avocados.urls')),
    url(r'^(?P<template_name>\w+)$', SimpleStaticView.as_view(template_name='anjular_site'), name='avocados'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
