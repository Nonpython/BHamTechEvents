#!/usr/bin/env python
# encoding: utf-8

from django.http import HttpResponse
from main.models.events import Event
from django.template import RequestContext
from django.template.loader import get_template
from itertools import chain
from math import log
from elementtree.SimpleXMLWriter import XMLWriter
import cStringIO
import utils.spellcheck
import json
from HTMLParser import HTMLParser

def index(request):
    t = get_template("base.html")
    c = RequestContext(request, {
        'loggedin': False,
        'title': "Home Page - Bellingham Tech Events"
    })
    return HttpResponse(t.render(c))

def tagcloud(threshold=0, maxsize=1.75, minsize=.75):
    """usage:
        -threshold: Tag usage less than the threshold is excluded from
            being displayed.  A value of 0 displays all tags.
        -maxsize: max desired CSS font-size in em units
        -minsize: min desired CSS font-size in em units
    Returns a list of dictionaries of the tag, its count and
    calculated font-size.
    """
    counts, taglist, tagcloud = [], [], []
    tags = list(
            chain.from_iterable(
                    [event.tags.all() for event in Event.objects.all()]
                    )
            )
    for tag in tags:
        count = len(Event.objects.filter(tags__name__in=[tag.name]))
        count >= threshold and (counts.append(count), taglist.append(tag))
    if len(counts) > 0:
        maxcount = max(counts)
        mincount = min(counts)
        constant = log(maxcount - (mincount - 1))/(maxsize - minsize or 1)
        tagcount = zip(taglist, counts)
        for tag, count in tagcount:
            size = log(count - (mincount - 1))/constant + minsize
            tagcloud.append({'tag': tag, 'count': count, 'size': round(size, 7)})
        return tagcloud
    else:
        return []



def tagcloudxml(request):
    xml = cStringIO.StringIO()
    w = XMLWriter(xml)
    tags = w.start("tags")
    for tag in tagcloud():
        w.element("a",
            text=tag['tag'],
            attrs={'href': "http://www.bhamtechevents.org/browse_events/%s".format(tag['tag']),
                   'title': "%s topics".format(tag["count"]), 'rel': "tag",
                   'style': "font-size: %s".format(tag["size"])}
        )
    w.end()
    w.close(tags)
    w.flush()
    return HttpResponse(xml.read())


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def spellchecker(request):
    spellchecker = utils.spellcheck.Hunspell()
    suggestions = spellchecker.suggest(strip_tags(request.POST["tocheck"]))
    return HttpResponse(json.dumps(suggestions))