from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^$', 'tethys_wps.views.home', name='home'),
)