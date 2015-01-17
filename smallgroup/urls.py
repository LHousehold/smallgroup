#from django.conf.urls import include, url
#from django.contrib import admin

#urlpatterns = [
    # Examples:
    # url(r'^$', 'smallgroup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    '',
#    url(r'^leaders/', include('leaders.urls')),
#    url(r'^admin/', include(admin.site.urls)),
#]


from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^', include('groups.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
