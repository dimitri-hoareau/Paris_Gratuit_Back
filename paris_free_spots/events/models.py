from django.db import models

class Event(models.Model):
    event_id = models.CharField(max_length=10, primary_key=True)
    url = models.URLField(max_length=500)
    title = models.CharField(max_length=500)
    lead_text = models.TextField()
    description = models.TextField(null=True, blank=True)
    date_start = models.DateTimeField(null=True, blank=True)
    date_end = models.DateTimeField(null=True, blank=True)
    occurrences = models.JSONField(null=True, blank=True)
    date_description = models.TextField(null=True, blank=True)
    cover_url = models.URLField(max_length=500, null=True, blank=True)
    cover_alt = models.CharField(max_length=500, null=True, blank=True)
    cover_credit = models.CharField(max_length=500, null=True, blank=True)
    tags = models.JSONField(null=True, blank=True)
    address_name = models.CharField(max_length=255)
    address_street = models.CharField(max_length=255)
    address_zipcode = models.CharField(max_length=50)
    address_city = models.CharField(max_length=100)
    price_type = models.CharField(max_length=100,null=True, blank=True)
    price_detail = models.CharField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.title
