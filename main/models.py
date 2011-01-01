from django.db import models
from markupfield.fields import MarkupField

class Location(models.Model):
	"A location where events take place"
	class Meta:
		verbose_name = ('location')
		verbose_name_plural = ('locations')
 	address      = models.CharField(max_length=255, blank=True)
	title        = models.CharField(max_length=255)
	slug         = models.SlugField(db_index=True)
	description  = MarkupField(markup_type="textile")
	location_img = models.ImageField(upload_to="uploads/")

class Tag(models.Model):
		name = models.CharField(max_length=255)
		
		def __unicode__(self):
			return u"Tag: %s" % name

class Event(models.Model):
	"One event"
	class Meta:
		verbose_name        = ('event')
		verbose_name_plural = ('events')
		ordering            = ('name',)
	name        = models.CharField(max_length=255)
	description = MarkupField(markup_type="textile")
	added       = models.DateTimeField(auto_now_add=True)
	location    = models.ForeignKey(Location)
	website     = models.URLField(verify_exists=True)
	tags		= models.ManyToManyField(Tag)
	freq        = models.CharField(max_length=7)
	# if freq = DAILY,   this doesn't matter.
	# if freq = WEEKLY,  this is the day of the week, in standard three letter form.
	# if freq = MONTHLY, this is a number, between 1 and 31 for recurrances like "The 23rd of every month".
	# or, a number between 1 and 4, followed by the oppropriate three letter day name for recurrances,
	# e.g. "The first Thursday of every month" would be 1Thu.
	# if freq = YEARLY, this is a number, between 1 and 365 for recurrances like "The 23rd day of the year".
	# or, a number between 1 and 53, followed by a three letter day name for recurrances like "The second thursday of April."
	# (Week numbers follow ISO.8601.2004)
	interval    = models.CharField(max_length=5)

class Occurrence(models.Model):
	occurrence_of = models.ForeignKey(Event)
	date          = models.DateField()
	start         = models.TimeField()
	end           = models.TimeField()
	
	def __unicode__(self):
		return u'Occurrence of Event "%s" on %s from %s to %s' % (occurrence_of.name, date, start, end)