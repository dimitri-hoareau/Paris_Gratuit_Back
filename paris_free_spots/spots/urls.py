from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DrinkingFountainViewSet, SanisetteViewSet

router = DefaultRouter()
router.register(r'drinking-fountains', DrinkingFountainViewSet)
router.register(r'sanisettes', SanisetteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
