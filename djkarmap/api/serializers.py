
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from main_app.models import Job


class JobSerializer(GeoFeatureModelSerializer):
    
    class Meta:
        model = Job
        geo_field = "location"
        fields =  '__all__'