from rest_framework import serializers
from .models import DrinkingFountain, Sanisette, WifiSpot

class DrinkingFountainSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkingFountain
        fields = '__all__'

class SanisetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sanisette
        fields = '__all__'

class WifiSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = WifiSpot
        fields = '__all__'
