from django.urls import path
from .views import JobPageListView, JobPageDetailView, AboutPageView, HomePageView, LoginView, SignUpView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('', JobPageListView.as_view(), name='jobs'),
    path('job/<int:pk>/', JobPageDetailView.as_view(), name='job_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
]