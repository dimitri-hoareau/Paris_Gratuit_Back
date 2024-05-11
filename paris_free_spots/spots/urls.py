from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DrinkingFountainViewSet

router = DefaultRouter()
router.register(r'drinking-fountains', DrinkingFountainViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
