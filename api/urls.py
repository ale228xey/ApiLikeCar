from django.urls import path
from rest_framework import routers

from api.viewsets import CarViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path('cars', CarViewSet.as_view()),
]
