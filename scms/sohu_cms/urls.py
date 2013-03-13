from django.conf.urls import patterns, include, url

urlpatterns = patterns(('scms.sohu_cms.views'),
    url(r'^list/$', 'article_list', name='list'), 
    url(r'^detail/(\d+)$', 'article_detail', name='detail'),
    url(r'^detail/(\d+)/(like|dislike)$', 'article_digg', name='digg'),
    url(r'^list/tag/$', 'article_taglist', name='taglist'),
    url(r'^list/tag/(.+)$', 'article_taglist', name='taglist'),
    url(r'^about/$', 'about'),
)
