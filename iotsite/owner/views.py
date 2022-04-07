from django.shortcuts import render
from rest_framework import viewsets
from .models import Position
from .serializers import PositionSerializer

# Create your views here.
class PositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint  allows groups to be viewed or edited.
    """
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

