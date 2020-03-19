from rest_framework import generics

from main_app.models import JobGroup

from .serializers import JobGroupSerializer



class JobGroupApiView(generics.ListAPIView):
    
    queryset = JobGroup.objects.all()
    serializer_class = JobGroupSerializer

