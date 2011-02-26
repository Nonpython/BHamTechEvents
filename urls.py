from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', 'main.views.index'),
    (r'^tagcloudxml', 'main.views.tagcloudxml')
    (r'user', 'main.views.user')
	(r'^login', 'main.views.login.login'),
	(r'^register', 'main.views.login.register ')
	(r'^register/activate', 'main.views.login.activate')
    (r'^view_event/(?P<event_id>\d+)', 'main.views.events.view_event'),
    (r'^add_event/', 'main.views.events.add_event'),
    (r'^browse_events/(?P<tag>.*)/', 'main.views.events.browse_events')
    (r'^view_venue/(?P<location_id>\d+)', 'main.views.venues.view_venue'),
    (r'^add_venue/', 'main.views.venues.add_venue'),
    (r'^browse_venues/', 'main.views.venues.browse_venue')
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls))
    )

