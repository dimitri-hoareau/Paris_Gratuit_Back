from rest_framework import serializers
from .models import DrinkingFountain, Sanisette, WifiSpot, LabHIV, Defibrillateur

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

class LabHIVSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabHIV
        fields = '__all__'

class DefibrillateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defibrillateur
        fields = '__all__'