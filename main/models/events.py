from django.db import models
from markupfield.fields import MarkupField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Location(models.Model):
    "A location where events take place"
    class Meta:
        verbose_name = ('location')
        verbose_name_plural = ('locations')
    address      = models.CharField(max_length=255, blank=True)
    title        = models.CharField(max_length=255)
    slug         = models.SlugField(db_index=True)
    description  = MarkupField(markup_type="markdown")
    location_img = models.ImageField(upload_to="uploads/")
    hasWifi      = models.BooleanField()
    cost         = models.PositiveSmallIntegerField()

class Event(models.Model):
    "One event"
    class Meta:
        verbose_name        = ('event',)
        verbose_name_plural = ('events',)
        ordering            = ('name',)
    name        = models.CharField(max_length=255)
    description = MarkupField(markup_type="markdown")
    added       = models.DateTimeField(auto_now_add=True)
    location    = models.ForeignKey(Location)
    website     = models.URLField(verify_exists=True)
    tags        = TaggableManager()
    start       = models.TimeField()
    end         = models.TimeField()
    freq        = models.CharField(max_length=7)
    # if freq = DAILY,   this doesn't matter.
    # if freq = WEEKLY,  this is the day of the week, in standard two letter form.
    # if freq = MONTHLY, this is a number between 1 and 4, followed by the oppropriate two letter day name.
    # e.g. "The first Thursday of every month" would be 1TH.
    # if freq = YEARLY, this is a number between 1 and 53, followed by a two letter day name for recurrances like "The second thursday of April."
    # That example would be something like "14TH" (Week numbers follow ISO.8601.2004)
    rule        = models.CharField(max_length=4)
    interval    = models.PositiveSmallIntegerField(default=1)
    owner = models.ForeignKey(User)

class Occurrence(models.Model):
    of   = models.ForeignKey(Event)
    date = models.DateField()
    def __unicode__(self):
        return u'Occurrence of Event "%s" on %s' % (self.of.name, self.date)