from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings

from groups import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^groups/$', views.groups),
    url(r'^signup/$', views.signup),
    url(r'^thankyou/$', views.thankyou),
    url(r'^contact/$', views.contact),
    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
