from rest_framework import serializers
from .models import DrinkingFountain

class DrinkingFountainSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkingFountain
        fields = ['id', 'object_type', 'street_number', 'street_name', 'city', 'available', 'longitude', 'latitude']
