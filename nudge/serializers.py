# < +------------------------------------------------------------+ >
# | Project: Nudge -- serializers.py
# | Description: Serializers for database integration
# | Author: Luke Ruter
# | Date: July 2019
# < +------------------------------------------------------------+ >

# < +------------------------------------------------------------+ >
# | Table of Contents
# | 1.  Imports
# | 2.  Serializers
# < +------------------------------------------------------------+ >

# < +------------------------------------------------------------+ >
# | Section 1: Imports
# < +------------------------------------------------------------+ >

from django.contrib.auth.models import User, Group
from nudge.models import Profile, Club, Event
from rest_framework import serializers

# < +------------------------------------------------------------+ >
# | Section 2: Serializers
# < +------------------------------------------------------------+ >

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'email', 'groups', 'profile')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name', 'description', 'banner', 'avatar')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('url', 'user', 'avatar', 'bio', 'user', 'phone', 'location')

class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ('url', 'name', 'avatar', 'banner', 'description', 'verified', 'members')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'name', 'host', 'location', 'start', 'end', 'image', 'tags', 'private')
