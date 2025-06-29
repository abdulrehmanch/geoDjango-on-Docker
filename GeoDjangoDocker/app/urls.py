from django.urls import path, include
from rest_framework import routers
from .views import LocationViewSet

router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]