from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', direct_to_template, {'template': 'index.html'}),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
)

"""
urlpatterns += patterns('cdi.apps.home.views',
        (r'^clubs/$', 'clubs_all'),
        (r'^clubs/all$', 'clubs_all'),
        (r'^clubs/popular/$', 'clubs_popular'),
        (r'^clubs/campus$', 'clubs_campus'),
        (r'^clubs/region$', 'clubs_region'),
        (r'^clubs/type$', 'clubs_types'),
        (r'^clubs/(\d)/$', 'clubs_detail'),
)
"""
