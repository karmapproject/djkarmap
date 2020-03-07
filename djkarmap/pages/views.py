from django.views.generic import TemplateView, ListView

from main_app.models import Job


class HomePageView(ListView):
    model = Job
    template_name = 'pages/home.html'
    context_object_name = 'all_Jobs'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'