from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', direct_to_template, {'template': 'pages.html'}),
     url(r'^about/$', direct_to_template, {'template': 'about.html'}),
     url(r'^team/$', direct_to_template, {'template': 'team.html'}),
     url(r'^contact/$', direct_to_template, {'template': 'contact.html'}),
     (r'^meta/$', 'cdi.views.extra'),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('cdi.home.views',
        (r'^clubs/$', 'clubs_popular'),
        (r'^clubs/all/$', 'clubs_all'),
        (r'^clubs/popular/$', 'clubs_popular'),
        (r'^clubs/campus/(\d)/$', 'clubs_campus'),
        (r'^clubs/region$', 'clubs_region'),
        (r'^clubs/type/(\d)/$', 'clubs_types'),
        (r'^clubs/(\d)/$', 'clubs_detail'),
)
