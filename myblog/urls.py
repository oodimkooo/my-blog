# coding: utf8
from django.conf.urls import url
from django.contrib import admin

from . import views
admin.autodiscover()

urlpatterns = [

    url(r'^$', views.PostListView.as_view(), name='list'),  # то есть по URL http://имя_сайта/blog/
    # будет выводиться список постов
    url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name="detail"),  # а по URL http://имя_сайта/blog/число/
    # будет выводиться пост с определенным номером
    url(r'^(?P<pk>\d+)/delete/$', views.delete_post,name='delete_post'),

    url(r'^(?P<pk>\d+)/vote/$', views.post_vote,name='post_vote'),

    url(r'^(?P<pk>\d+)/complete/$', views.post_vote,name='task_complete'),

    #формы создания и правки поста
    url(r'^new/$',views.add_post, name="new_post"),
    url(r'^(?P<pk>\d+)/edit/$',views.edit_post,{},name='edit_post'),

    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^register/$', views.register_user, name='register'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='list_draft'),

    url(r'^task_action/$', views.task_action ,name='task_action'),
    url(r'^search/(?P<tag>[a-zA-ZА-я0-9]+)/$', views.search_by_tag ,name='search_by_tag'),
    url(r'^search/$', views.PostSearchListView.as_view() ,name='search_by_text'),
    url(r'^tasks/(?P<pk>\d+)/$', views.TaskDetailView.as_view(), name="task_detail"),

    #Для задач - доработать шаблон
    #url(r'^tasks/(?P<pk>\d+)/$', views.TaskDetailView.as_view(), name='detail_task'),
]

