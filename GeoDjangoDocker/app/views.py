from django.shortcuts import render
from rest_framework import viewsets
from .models import Location
from .serializers import LocationSerializer

# Create your views here.
class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows locations to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
