from django.urls import path

from .views import WordAPIView


urlpatterns = [
    path('<str:mode>/<str:prev>/', WordAPIView.as_view()),
]
