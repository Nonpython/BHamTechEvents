#!/usr/bin/env python
# encoding: utf-8
from django.core.management.base import BaseCommand, CommandError
from main.models import Event, Occurance
from datetime import datetime
import dateutil
import dateutil.rrule
import re

class Command(BaseCommand):
        requires_model_validation = True
        help = 'Checks for events with less than NUM_OCCURANCES Occurances, and creates more' + \
        ' so that it has the correct number.'

        def handle(self, *args, **options):
            from django.conf import settings
            occurances = {}
            for event in Event.objects.all():
                            for occurance in event.occurances.all():
                                    try:
                                            occurances[occurance.of.name].append(occurance)
                                    except KeyError:
                                            occurances[occurance.of.name] = [occurance]
            for occurances_of_event in occurances.values():
                    occurances_of_event.sort(key=occurances.date)
                    for occurance in occurances_of_event:
                            if datetime.combine(occurance.date, occurance.of.start) < datetime.now(settings.TIME_ZONE):
                                    occurance.delete()
                                    print u'Removed Occurance of event "%s" at %s' % (occurance.of.name,
                                               datetime.combine(occurance.date, occurance.of.start))
                    if len(occurances_of_event) < getattr(settings, "MIN_EVENT_OCCURANCES", 3):
                        latest_occurance = occurances_of_event[-1]
                        if latest_occurance.of.freq == "DAILY":
                            rrule = dateutil.rrule.rrule(dateutil.rrule.DAILY,
                                                         count=1,
                                                         interval=latest_occurance.of.interval
                                                         )
                        elif latest_occurance.of.freq == "WEEKLY":
                             rrule = dateutil.rrule.rrule(dateutil.rrule.WEEKLY,
                                                         count=1,
                                                         byweekday=getattr(dateutil.rrule, latest_occurance.of.rule),
                                                         interval=latest_occurance.of.interval
                                                         )
                        elif latest_occurance.of.freq == "MONTHLY":
                            rrule = dateutil.rrule.rrule(dateutil.rrule.MONTHLY,
                                                         count=1,
                                                         byweekday=getattr(dateutil.rrule, latest_occurance.of.rule[1:]),
                                                         bysetpos=int(latest_occurance.of.rule[:1]),
                                                         interval=latest_occurance.of.interval
                                                         )
                        elif latest_occurance.of.freq == "YEARLY":
                            match = re.match(r'(\d\d?)([MO|TU|WE|TH|FR|SA|SU])', latest_occurance.of.interval)
                            rrule = dateutil.rrule.rrule(dateutil.rrule.YEARLY,
                                                         count=1,
                                                         byweekday=getattr(dateutil.rrule, match.group(2)),
                                                         byweekno=int(match.group(1)),
                                                         interval=latest_occurance.of.interval
                                                         )
                        occurance = Occurance(
                            of=latest_occurance.of,
                            date=rrule.after(datetime.combine(latest_occurance.of.date, latest_occurance.of.start)).date()
                        )
                        occurance.save()
                        print 'Added Occurance of Event "%s" on %s'  % (latest_occurance.of.name, occurance.date)

