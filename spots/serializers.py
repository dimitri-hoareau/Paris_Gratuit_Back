from rest_framework import serializers
from .models import DrinkingFountain, Sanisette, WifiSpot, LabHIV, Defibrillateur, OrganicWasteTrash, RecyclingTrash, TextileRecyclingTrash, SecondLifeCenter, SapinCollect

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

class OrganicWasteTrashSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganicWasteTrash
        fields = '__all__'

class RecyclingTrashSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecyclingTrash
        fields = '__all__'

class TextileRecyclingTrashSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextileRecyclingTrash
        fields = '__all__'

class SecondLifeCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondLifeCenter
        fields = '__all__'

class SapinCollectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SapinCollect
        fields = '__all__'