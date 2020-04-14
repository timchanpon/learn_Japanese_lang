from django.urls import path

from .views import WordAPIView


urlpatterns = [
    path('<int:word_count>/<str:pk>/', WordAPIView.as_view()),
]
