from django.db import models

class DrinkingFountain(models.Model):
    object_type = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=10)
    available = models.BooleanField(default=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f"{self.address} ({self.district})"





class Sanisette(models.Model):
    type = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=10)
    hours = models.CharField(max_length=50)
    access_pmr = models.BooleanField(default=False)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f"{self.address} ({self.district})"