import os

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(os.environ.get('ADMIN_SITE_PATH'), admin.site.urls),

    path('', include('home.urls')),
    path('words/', include('words.urls')),
    path('analytics/', include('analytics.urls')),
]
