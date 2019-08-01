from django.urls import include, path
from django.conf.urls import url
from django.shortcuts import render
from rest_framework import routers
from nudge import views
from django.conf import settings
from django.views import generic
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'clubs', views.ClubViewSet)
router.register(r'events', views.EventViewSet)

urlpatterns = [
    path('', views.goToHome, name='index'),
    path('home/', generic.TemplateView.as_view(template_name="nudge/home.html"), name='home'),

    path('manage/', views.ManageClubListView.as_view(), name='manage_club_list'),
    path('manage/preview/<pk>', views.ManageClubDetailView.as_view(), name='club_detail'),
    path('manage/update/<pk>', views.ManageClubDetailsUpdateView.as_view(), name='manage_club_update'),
    path('manage/members/<pk>', views.ManageClubMembersUpdateView.as_view(), name='manage_club_members_update'),
    path('manage/events/<pk>', views.ManageClubEventsUpdateView.as_view(), name='manage_club_events_update'),

    path('explore/', generic.RedirectView.as_view(url='./clubs/', permanent=False), name="explore"),
    path('explore/clubs/', views.ExploreClubListView.as_view(), name="explore_club_list"),
    path('explore/events/', views.ExploreEventListView.as_view(), name="explore_event_list"),
    path('explore/clubs/<pk>', views.ExploreClubDetailView.as_view(), name='explore_club_detail'),
    path('explore/events/<pk>', views.ExploreEventDetailView.as_view(), name='explore_event_detail'),

    path('profile/', generic.TemplateView.as_view(template_name="nudge/profile/profile.html"), name='profile'),

    path('api/', include(router.urls)),
    url(r'^auth/', include('social_django.urls', namespace='social')),
]
