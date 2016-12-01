# coding: utf8
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from imagepool.views import Image_Upload,delete_image,Image_List,Image_Detail
from . import views


admin.autodiscover()

urlpatterns = [
    url(r'^$', Image_List.as_view(), name='image_index'),
    url(r'^upload/$', Image_Upload.as_view(), name='image_upload'),
    url(r'^(?P<pk>\d+)/$', Image_Detail.as_view(), name="image_detail"),
    url(r'^(?P<pk>\d+)/delete/$', delete_image, name='image_delete'),
    url(r'^logout/$', views.logout_user, name='logout'),
]

