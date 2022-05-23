from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from Car.models import Car
from api.serializers import CarSerializer


class CarViewSet(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
