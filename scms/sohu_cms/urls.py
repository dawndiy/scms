from django.conf.urls import patterns, include, url

urlpatterns = patterns(('scms.sohu_cms.views'),
    url(r'^articlelist/$', 'article_list', name='articlelist'), 
)
