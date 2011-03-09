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
    tags = TaggableManager()
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

class Occurrence(models.Model):
    of   = models.ForeignKey(Event)
    date = models.DateField()
    def __unicode__(self):
        return u'Occurrence of Event "%s" on %s' % (self.of.name, self.date)

class UserProfile(models.Model):
    home_address = models.TextField()
    likes = models.ManyToManyField(Event)
    user = models.ForeignKey(User, unique=True)

from django.contrib.comments.signals import comment_was_posted

def on_comment_was_posted(sender, comment, request, *args, **kwargs):
    # spam checking can be enabled/disabled per the comment's target Model
    #if comment.content_type.model_class() != Entry:
    #    return
    from django.contrib.sites.models import Site
    from django.conf import settings
    try:
        from akismet import Akismet
    except:
        return
    # use TypePad's AntiSpam if the key is specified in settings.py
    if hasattr(settings, 'TYPEPAD_ANTISPAM_API_KEY'):
        ak = Akismet(
            key=settings.TYPEPAD_ANTISPAM_API_KEY,
            blog_url='http://%s/' % Site.objects.get(pk=settings.SITE_ID).domain
        )
        ak.baseurl = 'api.antispam.typepad.com/1.1/'
    else:
        ak = Akismet(
            key=settings.AKISMET_API_KEY,
            blog_url='http://%s/' % Site.objects.get(pk=settings.SITE_ID).domain
        )
    if ak.verify_key():
        data = {
            'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
            'user_agent': request.META.get('HTTP_USER_AGENT', ''),
            'referrer': request.META.get('HTTP_REFERER', ''),
            'comment_type': 'comment',
            'comment_author': comment.user_name.encode('utf-8'),
        }
        if ak.comment_check(comment.comment.encode('utf-8'), data=data, build_data=True):
            comment.flags.create(
                user=comment.content_object.author,
                flag='spam'
            )
            comment.is_public = False
            comment.save()

comment_was_posted.connect(on_comment_was_posted)
