from django.conf.urls.defaults import *
from django.conf import settings

from main.feeds import RSSEventsFeed, AtomEventsFeed, iCalEventsFeed

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'main.views.shared.index'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    (r'^tagcloudxml$', 'main.views.shared.tagcloudxml'),
    (r'^feeds/atom', AtomEventsFeed()),
    (r'^feeds/ical', iCalEventsFeed()),
    (r'^feeds/rss', RSSEventsFeed()),
    (r'^user$', 'main.views.user'),
    (r'^login$', 'main.views.login.login'),
    (r'^register$', 'main.views.login.register '),
    (r'^register/activate$', 'main.views.login.activate'),
    (r'^events/view/(?P<event_id>\d+)$', 'main.views.events.view_event'),
    (r'^events/add$', 'main.views.events.add_event'),
    (r'^events/browse$', 'main.views.events.browse_events'),
    (r'^events/bytag/(?P<tag>.*)/$', 'main.views.events.browse_events_by_tag'),
    (r'^venues/view/(?P<location_id>\d+)$', 'main.views.venues.view_venue'),
    (r'^venues/add$', 'main.views.venues.add_venue'),
    (r'^venues/browse$', 'main.views.venues.browse_venue'),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    )

