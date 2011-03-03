#!/usr/bin/env python
# encoding: utf-8

from django.http import HttpResponse
from elementtree.SimpleXMLWriter import XMLWriter
import cStringIO
from main.models import Event
from math import log
from django.template import RequestContext
from django.template.loader import get_template

def index(request):
    t = get_template("base.html")
    c = RequestContext(request, {
        'loggedin': False,
    })
    return HttpResponse(t.render(c))

