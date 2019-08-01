# < +------------------------------------------------------------+ >
# | Project: Nudge -- views.py
# | Description: Views for web app and API.
# | Author: Luke Ruter
# | Date: April 2019
# < +------------------------------------------------------------+ >

# < +------------------------------------------------------------+ >
# | Table of Contents
# | 1.  Imports
# | 1a. Custom Views
# | 2.  Manager Views
# | 2.  User Views
# | 3.  API ViewSets
# < +------------------------------------------------------------+ >

# < +------------------------------------------------------------+ >
# | Section 1: Imports
# < +------------------------------------------------------------+ >

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from nudge.models import Profile, Club, Event, Membership
from nudge.serializers import UserSerializer, GroupSerializer, EventSerializer, ClubSerializer, ProfileSerializer
from django.urls import reverse_lazy
from material.frontend.views import UpdateModelView, CreateModelView, DetailModelView, ListModelView
from nudge.models import Club
from django.views import generic
from django.urls import reverse

# < +------------------------------------------------------------+ >
# | Section 1a: Custom Views
# < +------------------------------------------------------------+ >

def goToHome(request):
    context = dict()
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    else:
        return HttpResponseRedirect('/accounts/login/')

# < +------------------------------------------------------------+ >
# | Section 2: Manager Views
# < +------------------------------------------------------------+ >

class ManageClubListView(ListModelView):
    model = Club
    list_display = ('name',)
    template_name = "nudge/manage/index.html"
    def get_item_url(self, item):
        opts = self.model._meta
        return reverse(
            '{}:manage_{}_update'.format(opts.app_label, opts.model_name),
            args=[item.pk])
    def get_context_data(self, **kwargs):
        return super(ListModelView, self).get_context_data(**kwargs)

class ManageClubDetailView(DetailModelView):
    model = Club
    template_name = "nudge/manage/club_detail.html"
    def get_context_data(self, **kwargs):
        opts = self.model._meta
        kwargs['object_data'] = self.get_object_data()
        return super(DetailModelView, self).get_context_data(**kwargs)

class ManageClubDetailsUpdateView(UpdateModelView):
    model = Club
    fields = ['name', 'description', 'banner', 'avatar']
    template_name = "nudge/manage/club_update.html"

class ManageClubMembersUpdateView(UpdateModelView):
    model = Membership
    fields = ['members']
    template_name = "nudge/manage/club_members.html"

class ManageClubEventsUpdateView(UpdateModelView):
    model = Club
    fields = ['events']
    template_name = "nudge/manage/club_events.html"

# < +------------------------------------------------------------+ >
# | Section 1: User Views
# < +------------------------------------------------------------+ >

class ExploreClubListView(ListModelView):
    model = Club
    list_display = ('name', 'description',)
    template_name = "nudge/explore/club_list.html"
    def get_item_url(self, item):
        opts = self.model._meta
        return reverse(
            '{}:explore_{}_detail'.format(opts.app_label, opts.model_name),
            args=[item.pk])
    def get_context_data(self, **kwargs):
        return super(ListModelView, self).get_context_data(**kwargs)

class ExploreEventListView(ListModelView):
    model = Event
    list_display = ('name', 'location', 'start', 'end', 'tags')
    template_name = "nudge/explore/event_list.html"
    def get_context_data(self, **kwargs):
        return super(ListModelView, self).get_context_data(**kwargs)

class ExploreClubDetailView(DetailModelView):
    model = Club
    template_name = "nudge/explore/club_detail.html"
    def get_context_data(self, **kwargs):
        opts = self.model._meta
        kwargs['object_data'] = self.get_object_data()
        return super(DetailModelView, self).get_context_data(**kwargs)

class ExploreEventDetailView(DetailModelView):
    model = Event
    template_name = "nudge/explore/event_detail.html"
    def get_context_data(self, **kwargs):
        opts = self.model._meta
        kwargs['object_data'] = self.get_object_data()
        return super(DetailModelView, self).get_context_data(**kwargs)

# < +------------------------------------------------------------+ >
# | Section 1: API ViewSets
# < +------------------------------------------------------------+ >

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-last_name')
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all().order_by('name')
    serializer_class = ClubSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('start')
    serializer_class = EventSerializer
