# coding: utf8
from django.conf.urls import url
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index),
    url(r'^get_events/$', views.get_events, name = "get_events"),
    url(r'^set_event/$', views.set_event, name = "set_event"),
]
