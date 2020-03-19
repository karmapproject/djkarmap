from rest_framework import generics

from main_app.models import Job

from .serializers import JobSerializer


# TODO use post or get is better
class JobApiView(generics.ListAPIView):

    serializer_class = JobSerializer

    def get_queryset(self):
        # save parameters sended by search form
        group = self.kwargs['group']
        user_type = self.kwargs['user_type']
        # when user select employee he want find jobs requested by employer
        # so in form we use 1 for 'KJ and 2 for 'KF'
        # and so so we changed it for get require queryset

        if user_type == 1:
            user_type = 'KF'
        else:
            user_type = 'KJ'        
        
        return Job.objects.filter(user__user_type=user_type, group=group)[0:100]


class JobDetailView(generics.RetrieveAPIView):

    queryset = Job.objects.all()
    serializer_class = JobSerializer
