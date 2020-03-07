from django.views.generic import TemplateView, ListView, DetailView

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