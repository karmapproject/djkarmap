
from rest_framework import serializers

from main_app.models import Job


class JobSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Job
        fields =  '__all__'