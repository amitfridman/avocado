
from . import settings
from django.views.static import serve
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf.urls import url
from django.views.generic import TemplateView
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
    url(r'^(?P<template_name>\w+)$', SimpleStaticView.as_view(
        template_name='anjular_site'), name='avocados'),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
    url("favicon.ico", RedirectView.as_view(url=r'^static/favicon.ico')),
 ]
