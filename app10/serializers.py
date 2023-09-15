from rest_framework import serializers
from .models import Models10

class Serializers10(serializers.ModelSerializer):
    class Meta:
        model = Models10
        fields = ("__all__")