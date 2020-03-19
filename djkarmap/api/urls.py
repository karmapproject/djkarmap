from django.urls import path
from . views import JobApiView, JobDetailView

urlpatterns = [
    path('job/',  JobApiView.as_view()),
    path('job/<int:pk>/', JobDetailView.as_view()),
]
