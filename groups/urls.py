from django.conf.urls import patterns, url

from groups import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^groups', views.groups),
    )
