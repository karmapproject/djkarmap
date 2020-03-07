from django.views.generic import TemplateView, ListView

# from main_app.models import JobOrder


# class HomePageView(ListView):
#     model = JobOrder
#     template_name = 'pages/home.html'
#     context_object_name = 'all_orders'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'