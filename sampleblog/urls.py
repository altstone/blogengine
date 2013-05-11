# coding=utf-8
from django.conf.urls import patterns, url

from views import (PostListView, PostCreateView, PostDetailView,
    PostUpdateView, PostDeleteView)


urlpatterns = patterns('',
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^create$', PostCreateView.as_view(), name='post_create'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^(?P<pk>\d+)/edit/$', PostUpdateView.as_view(), name='post_update'),
    url(r'^(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='post_delete'),
)
