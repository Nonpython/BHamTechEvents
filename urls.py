from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', 'main.views.index'),
    (r'^view/(?P<event_id>\d+)', 'main.views.viewevent'),
    (r'^add/', 'main.views.addevent'),
    (r'^viewlocation/(?P<location_id>\d+)', 'main.views.viewlocation'),
    (r'^addlocation/', 'main.views.addlocation'),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls))
    )
