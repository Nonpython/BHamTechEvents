from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    picture = models.ImageField(upload_to="user_photos/")

    home_address = models.TextField()
    can_carpool = models.BooleanField()
    num_seats = models.PositiveSmallIntegerField()

    likes = models.ManyToManyField(Event)
