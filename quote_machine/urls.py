# coding: utf8
from django.conf.urls import url
from django.contrib import admin

from .views import QuoteView, get_next_quote, set_new_quote
admin.autodiscover()

urlpatterns = [
    url(r'^$', QuoteView.as_view(), name='quotes'),
    url(r'^get/$', get_next_quote, name='get_quotes'),
    url(r'^set/$', set_new_quote, name='set_quotes'),
]
