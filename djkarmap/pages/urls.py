from django.urls import path
from .views import JobPageListView, JobPageDetailView, AboutPageView

urlpatterns = [
    path('', JobPageListView.as_view(), name='jobs'),
    path('job/<int:pk>/', JobPageDetailView.as_view(), name='job_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
]