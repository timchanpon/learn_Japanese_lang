from django.urls import path

from .views import WordAPIView


urlpatterns = [
    path('<str:pk>/', WordAPIView.as_view()),
]
