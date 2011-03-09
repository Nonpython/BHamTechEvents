from django.db import models
from django.contrib.auth.models import User

class Picture(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="photos/")

class TaggedPerson(models.Model):
    top = models.IntegerField()
    left = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    image = models.ForeignKey(Picture, primary_key=True)
    person = models.ForeignKey(User)