from django.urls import path
from . views import JobGroupApiView

urlpatterns = [
    path('job_group',  JobGroupApiView.as_view()),
]
