from django.contrib import admin
from .models import DrinkingFountain, Sanisette, WifiSpot, LabHIV, Defibrillateur

# Register your models here.


admin.site.register(DrinkingFountain)
admin.site.register(Sanisette)
admin.site.register(WifiSpot)
admin.site.register(LabHIV)
admin.site.register(Defibrillateur)