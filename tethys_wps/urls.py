from django.conf.urls import patterns, url, include

service_urls = [
    url(r'^$', 'tethys_wps.views.service', name='service'),
    url(r'^process/(?P<identifier>[\w.]+)/$', 'tethys_wps.views.process', name='process')
]

urlpatterns = patterns('',
    url(r'^$', 'tethys_wps.views.home', name='home'),
    url(r'^(?P<service>\w+)/', include(service_urls)),
)