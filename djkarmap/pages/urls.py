from django.urls import path
from .views import JobPageListView, JobPageDetailView, AboutPageView, JustForTestTemplateInherit

urlpatterns = [
    path('', JustForTestTemplateInherit.as_view(), name='alaki'),
    # path('', JobPageListView.as_view(), name='jobs'),
    path('job/<int:pk>/', JobPageDetailView.as_view(), name='job_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
]