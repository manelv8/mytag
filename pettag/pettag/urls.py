from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'mytag.views.index'),
     url(r'^registrar/$', 'mytag.views.registrar'),
     url(r'^login/$', 'mytag.views.login'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
