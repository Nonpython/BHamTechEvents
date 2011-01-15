#!/usr/bin/env python
# encoding: utf-8
from django.http import HttpResponse
from elementtree.SimpleXMLWriter import XMLWriter
import cStringIO
from main.models import Event
from math import log

def index(request):
    return HttpResponse("Hello, world. You're at the index of bhamtechevents.org!")

	def tagcloud(tags, threshold=0, maxsize=4, minsize=.75):
	    """usage: 
	        -threshold: Tag usage less than the threshold is excluded from
	            being displayed.  A value of 0 displays all tags.
	        -maxsize: max desired CSS font-size in em units
	        -minsize: min desired CSS font-size in em units
	    Returns a list of dictionaries of the tag, its count and
	    calculated font-size.
	    """
	    counts, taglist, tagcloud = [], [], []
	    for tag in tags:
	        count = tag.items.count()
	        count >= threshold and (counts.append(count), taglist.append(tag))
	    maxcount = max(counts)
	    mincount = min(counts)
	    constant = log(maxcount - (mincount - 1))/(maxsize - minsize or 1)
	    tagcount = zip(taglist, counts)
	    for tag, count in tagcount:
	        size = log(count - (mincount - 1))/constant + minsize
	        tagcloud.append({'tag': tag, 'count': count, 'size': round(size, 7)})
	    return tagcloud


def tagcloudxml(request):
	xml = cStringIO.StringIO()
	w = XMLWriter(xml)
	tags = w.start("tags")
	for tag in tagcloud(Event.tags.all()):
		w.element("a", 
		text=tag[tag],
		name="href", value="http://www.bhamtechevents.org/browse_events/%s".format(tag[tag]),
		name="title", value="%s topics".format(tag[count]),
		name="rel", value="tag",
		name="style", value="font-size: %s".format(tag[size])
		)
	w.end()
	w.close(tags)
	return ''.join(xml.readlines())
	