from django.urls import path
from .views import AnimesViewSet

urlpatterns = [
    path('animes/', AnimesViewSet.as_view()),
    path('animes/<int:id>/', AnimesViewSet.as_view())
]