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