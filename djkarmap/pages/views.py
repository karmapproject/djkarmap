from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from main_app.models import Job






class JobPageListView(ListView):
    model = Job
    template_name = 'pages/jobs.html'
    context_object_name = 'all_Jobs'


class JobPageDetailView(DetailView):

    template_name = 'pages/job_detail.html'
    context_object_name = 'job'
    queryset = Job.objects.order_by('-created')
    

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class LoginView(TemplateView):
    template_name = 'pages/login.html'


class HomePageView(TemplateView):
    template_name = 'pages/home/home.html'



class SignUpView(CreateView):

    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'pages/signup.html'