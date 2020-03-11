
from django.views.generic import ListView

from main_app.models import JobOrder


class JobOrderListView(ListView):
    model = JobOrder
    template_name = 'home.html'
