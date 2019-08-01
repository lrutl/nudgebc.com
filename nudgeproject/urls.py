from django.contrib import admin
from django.urls import include, path
from django.conf.urls import include, url
from django.views import generic
from material.frontend import urls as frontend_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    url(r'', include(frontend_urls)),
    path('', include('nudge.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
