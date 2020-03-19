from rest_framework import generics

from main_app.models import Job

from .serializers import JobSerializer



class JobApiView(generics.ListAPIView):

    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetailView(generics.RetrieveAPIView):

    queryset = Job.objects.all()
    serializer_class = JobSerializer
