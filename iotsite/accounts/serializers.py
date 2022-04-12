from .models import Account
from rest_framework import serializers

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'password', 'user_type', 'is_active']