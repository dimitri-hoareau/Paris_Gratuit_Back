from django.db import models

class DrinkingFountain(models.Model):
    object_type = models.CharField(max_length=50)
    street_number = models.CharField(max_length=10)
    street_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f"{self.street_number} {self.street_name}, {self.city}"
