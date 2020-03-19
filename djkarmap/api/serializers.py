
from rest_framework import serializers

from main_app.models import JobGroup


class JobGroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobGroup
        fields = ('title',)