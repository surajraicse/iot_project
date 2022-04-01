from django.shortcuts import render
from django.contrib.auth.models import Position
from rest_framework import viewsets
from iotsite.owner.serializers import PositionSerializer

# Create your views here.
class PositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint  allows groups to be viewed or edited.
    """
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

