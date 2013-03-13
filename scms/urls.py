from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scms.views.home', name='home'),
    # url(r'^scms/', include('scms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # sohu news
    url(r'^sohu/', include('scms.sohu_cms.urls')),
    url(r'^$', 'scms.sohu_cms.views.article_list'),
)
