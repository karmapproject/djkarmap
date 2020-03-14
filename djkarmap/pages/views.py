
from django.shortcuts import render

from main_app.models import JobGroup, JobOrder



def home(request):
    latest_job_groups = JobGroup.objects.all()
    latest_job_order = JobOrder.objects.order_by('-created')[:5]

    context = {
        'latest_job_group': latest_job_groups,
        'latest_job_order': latest_job_order,

    }

    return render(request, 'home.html', context)


