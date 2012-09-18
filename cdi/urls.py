from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', direct_to_template, {'template': 'home.html'}),
     url(r'^about/$', direct_to_template, {'template': 'about.html'}),
     url(r'^team/$', direct_to_template, {'template': 'team.html'}),
     url(r'^contact/$', direct_to_template, {'template': 'contact.html'}),
     url(r'^academics/', direct_to_template, {'template': 'coming.html'}),
     (r'^meta/$', 'cdi.views.extra'),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('cdi.home.views',
        (r'^clubs/$', 'clubs_all'),
        (r'^clubs/all/$', 'clubs_all'),
        (r'^clubs/popular/$', 'clubs_popular'),
        (r'^clubs/campus/(\d)/$', 'clubs_campus'),
        (r'^clubs/region/(\d)/$', 'clubs_region'),
        (r'^clubs/type/(\d)/$', 'clubs_types'),
        (r'^clubs/(\d)/$', 'clubs_detail'),
)

urlpatterns += patterns('cdi.home.views',
        (r'^events/$', 'events_all'),
        (r'^events/all/$', 'events_all'),
        (r'^events/coming/$', 'events_all'),
        (r'^events/popular/$', 'events_popular'),
        (r'^events/campus/(\d)/$', 'events_campus'),
#        (r'^events/region/(\d)/$', 'events_region'),
        (r'^events/type/(\d)/$', 'events_types'),
        (r'^events/(\d)/$', 'events_detail'),
)

urlpatterns += patterns('cdi.home.views',
        (r'^colleges/$', 'colleges_all'),
        (r'^colleges/all/$', 'colleges_all'),
        (r'^colleges/popular/$', 'colleges_popular'),
        (r'^colleges/type/(\d)/$', 'colleges_types'),
        (r'^colleges/(\d)/$', 'colleges_detail'),
)

