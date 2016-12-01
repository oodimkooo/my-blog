# coding: utf8
from django.conf.urls import url
from django.contrib import admin

from . import views
admin.autodiscover()

urlpatterns = [

    url(r'^$', views.PostListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name="detail"),
    url(r'^(?P<pk>\d+)/delete/$', views.delete_post,name='delete_post'),
    url(r'^(?P<pk>\d+)/vote/$', views.post_vote,name='post_vote'),

    url(r'^new/$',views.add_post, name="new_post"),
    url(r'^(?P<pk>\d+)/edit/$',views.edit_post,{},name='edit_post'),
    #url(r'^login/$', views.ajax_login,{}, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    #url(r'^register/$', views.register_user, name='register'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='list_draft'),
    url(r'^search/(?P<tag>[a-zA-ZА-я0-9]+)/$', views.SearchByTagListView.as_view() ,name='search_by_tag'),
    url(r'^categories/(?P<category>[a-zA-ZА-я0-9]+)/$', views.CategoryListView.as_view() ,name='search_by_category'),
    url(r'^search/$', views.SearchByTextListView.as_view() ,name='search_by_text'),

    #url(r'^(?P<pk>\d+)/complete/$', views.post_vote,name='task_complete'),
    #url(r'^task_action/$', views.task_action ,name='task_action'),
    #url(r'^tasks/(?P<pk>\d+)/$', views.TaskDetailView.as_view(), name="task_detail"),
]

