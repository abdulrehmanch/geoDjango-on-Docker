from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Location

class LocationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Location
        geo_field = "point"
        fields = ('id', 'name', 'description', 'point', 'created_at', 'updated_at')