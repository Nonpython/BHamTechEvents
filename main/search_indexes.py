#!/usr/bin/env python
# encoding: utf-8
import datetime
from haystack import indexes
from haystack import site
from main.models import Event

class EventIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True)
    def get_queryset(self):
        """Used when the entire index for model is updated."""
        return Event.objects.filter(added_lte=datetime.datetime.now())

site.register(Event, EventIndex)
