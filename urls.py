from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^index', 'main.views.shared.index'),
    (r'^tagcloudxml', 'main.views.tagcloudxml')
    #(r'user', 'main.views.user')
	#(r'^login', 'main.views.login.login'),
	#(r'^register', 'main.views.login.register ')
	#(r'^register/activate', 'main.views.login.activate')
    #(r'^events/view/(?P<event_id>\d+)', 'main.views.events.view_event'),
    #(r'^events/add', 'main.views.events.add_event'),
    #(r'^events/browse', 'main.views.events.browse_events')
    #(r'^events/bytag/(?P<tag>.*)/', 'main.views.events.browse_events_by_tag')
    #(r'^venues/view/(?P<location_id>\d+)', 'main.views.venues.view_venue'),
    #(r'^venues/add', 'main.views.venues.add_venue'),
    #(r'^venues/browse', 'main.views.venues.browse_venue')
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #(r'^admin/', include(admin.site.urls))
    )

