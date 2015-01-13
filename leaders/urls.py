from django.conf.urls import patterns, url

from leaders import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^leader/', views.leader),
    )
