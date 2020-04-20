from django.urls import path

from .views import AnalyticsAPIView


urlpatterns = [
    path('', AnalyticsAPIView.as_view()),
]
