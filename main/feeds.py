#!/usr/bin/env python
from django.template.context import Context
from main.models import Occurrence
from django.template import Template
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed

from datetime import datetime
from dateutil.relativedelta import relativedelta
import vobject


# iCalendar feed
EVENT_ITEMS = (
    ('uid', 'uid'),
    ('dtstart', 'start'),
    ('dtend', 'end'),
    ('summary', 'summary'),
    ('location', 'location'),
    ('last_modified', 'last_modified'),
    ('created', 'created'),
)

class ICalendarFeed(object):

    def __call__(self, *args, **kwargs):

        cal = vobject.iCalendar()

        for item in self.items():

            event = cal.add('vevent')

            for vkey, key in EVENT_ITEMS:
                value = getattr(self, 'item_' + key)(item)
                if value:
                    event.add(vkey).value = value

        response = HttpResponse(cal.serialize())
        response['Content-Type'] = 'text/calendar'

        return response

    def items(self):
        return []

    def item_uid(self, item):
        pass

    def item_start(self, item):
        pass

    def item_end(self, item):
        pass

    def item_summary(self, item):
        return str(item)

    def item_location(self, item):
        pass

    def item_last_modified(self, item):
        pass

    def item_created(self, item):
        pass

class RSSEventsFeed(Feed):
    title = "bhamtechevents.org Upcoming Events"
    description = "Upcoming events in the Bellingham, WA area."
    link = "http://www.bhamtechevents.org/rss_feed"

    def items(self):
        return Occurrence.objects.filter(date__lte=datetime.now()+relativedelta(months=+1))

    def item_title(self, item):
        return "\"" + item.of.name + "\" is meeting at \"" + item.of.location.name + "\" (http://www.bhamtechevents.org/events/view/" + item.of.id

    def item_description(self, item):
        t = Template('''
        {% load humanize %}
        <p>
            <a href="http://www.bhamtechevents.org/events/view/{{ item.of.id }}">
                "{{ item.of.name }}"
            </a>
            is meeting at
            <a href="http://www.bhamtechevents.org/venues/view/{{ item.of.location.id }}">
                "{{ item.of.location.name }}"
            </a>
            from {{ item.of.start | time: "h:i A" }} to {{ item.of.start | time: "h:i A" }} on
            {{ item.date | naturalday: "l, F j, Y"}}.''')
        c = Context(
            {
                    "item": item
            }
        )
        return t.render(c)


class AtomEventsFeed(RSSEventsFeed):
    feed_type = Atom1Feed
    subtitle = RSSEventsFeed.description
    link = "http://www.bhamtechevents.org/atom_feed"

class iCalEventsFeed(RSSEventsFeed, ICalendarFeed):
    def item_uid(self, item):
        return str(item.id)

    def item_start(self, item):
        return datetime.combine(item.start, item.of.start)

    def item_end(self, item):
        return datetime.combine(item.end, item.of.end)
