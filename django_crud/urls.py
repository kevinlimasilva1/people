"""django_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'cadastro.views.home', name = 'cadastro_home'),
    url(r'^cadastro/$', 'cadastro.views.lista', name = 'cadastro_lista'),
    url(r'^cadastro_novo/$', 'cadastro.views.novo', name = 'cadastro_novo'),
    url(r'^cadastro/(?P<pk>\d+)/$', 'cadastro.views.detalhe', name = 'cadastro_detalhe'),
    url(r'^cadastro_deletar/(?P<pk>\d+)/$', 'cadastro.views.deletar', name = 'cadastro_deletar'),
    url(r'^cadastro_atualizar/(?P<pk>\d+)/$', 'cadastro.views.atualizar', name = 'cadastro_atualizar'),
]
