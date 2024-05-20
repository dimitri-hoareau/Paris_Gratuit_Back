from django.db import models

class DrinkingFountain(models.Model):
    fountain_id = models.CharField(max_length=100,unique=True, null=False)
    object_type = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=255, null=True)
    district = models.CharField(max_length=50, null=True)
    available = models.BooleanField(default=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f"{self.address} ({self.district})"

class Sanisette(models.Model):
    sanisette_id = models.CharField(max_length=100,unique=True, null=False)
    type = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255, null=True)
    district = models.CharField(max_length=50, null=True)
    hours = models.CharField(max_length=50, null=True)
    access_pmr = models.BooleanField(default=False)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f"{self.address} ({self.district})"
    
class WifiSpot(models.Model):
    wifi_id = models.CharField(max_length=100,unique=True, null=False)
    spot_name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255, null=True)
    district = models.CharField(max_length=50, null=True)
    state = models.BooleanField(default=False)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f"{self.spot_name} ({self.district})"
    

class LabHIV(models.Model):
    lab_id = models.CharField(max_length=100,unique=True, null=False)
    lab_name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255, null=True)
    district = models.CharField(max_length=50, null=True)
    hours = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=50, null=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f"{self.lab_name} ({self.district})"
    

class Defibrillateur(models.Model):
    def_id = models.CharField(max_length=100,unique=True, null=False)
    spot_name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255, null=True)
    district = models.CharField(max_length=50, null=True)
    state = models.BooleanField(default=False)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f"{self.spot_name} ({self.district})"
    
