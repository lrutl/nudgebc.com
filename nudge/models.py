# < +------------------------------------------------------------+ >
# | Project: Nudge -- models.py
# | Description: Django model declarations
# | Author: Luke Ruter
# | Date: April 2019
# < +------------------------------------------------------------+ >

# < +------------------------------------------------------------+ >
# | Table of Contents
# | 1.  Imports
# | 2.  Profile Model
# | 2.  Event Model
# | 3.  Club Model
# | 4.  Relational Models
# < +------------------------------------------------------------+ >

# < +------------------------------------------------------------+ >
# | Section 1: Imports
# < +------------------------------------------------------------+ >

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.fields import ArrayField

# < +------------------------------------------------------------+ >
# | Section 1: Profile
# < +------------------------------------------------------------+ >

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    YEAR_CHOICES = (('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), )
    year = models.CharField(max_length=2, choices=YEAR_CHOICES, default='FR',)
    avatar = models.ImageField(upload_to='user_avatars', blank=True, null=True)
    banner = models.ImageField(upload_to='user_banners', blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.user.email

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# < +------------------------------------------------------------+ >
# | Section 2: Event
# < +------------------------------------------------------------+ >

class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=8000)
    start = models.DateTimeField()
    end = models.DateTimeField()
    image = models.ImageField()
    tags = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    class Meta:
        ordering = ('start',)
    def __str__(self):
        return self.name

# < +------------------------------------------------------------+ >
# | Section 3: Club
# < +------------------------------------------------------------+ >

class Club(models.Model):
    name = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='club_avatars', blank=True, null=True)
    banner = models.ImageField(upload_to='club_banners', blank=True, null=True)
    description = models.CharField(max_length=8000)
    verified = models.BooleanField(default=False)
    events = models.ManyToManyField(Event, through='ClubEvents', through_fields=('club', 'event', 'private'),)
    members = models.ManyToManyField(Profile, through='Membership', through_fields=('club', 'profile', 'position', 'perms'),)
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

# < +------------------------------------------------------------+ >
# | Section 4: Relational
# < +------------------------------------------------------------+ >

class ClubEvents(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    private = models.BooleanField(default=False)

class Membership(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    position = models.CharField(max_length=200, default="Member")
    perms = models.BooleanField(default=False)
    inviter = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="membership_invites",)
    invite_reason = models.CharField(max_length=64)
