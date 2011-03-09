from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    home_address = models.TextField()
    likes = models.ManyToManyField(Event)
    user = models.ForeignKey(User, unique=True)