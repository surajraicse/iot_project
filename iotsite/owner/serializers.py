from .models import Position
from rest_framework import serializers

class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ['plate_id', 'longitude', 'latitude', 'speed']
