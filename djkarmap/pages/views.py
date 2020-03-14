
from django.shortcuts import render
from django.http import HttpResponseRedirect

from main_app.models import JobGroup, JobOrder
from main_app.forms import EmployeeForm



def home(request):
    latest_job_groups = JobGroup.objects.all()
    latest_job_order = JobOrder.objects.order_by('-created')[:5]

    context = {
        'latest_job_group': latest_job_groups,
        'latest_job_order': latest_job_order,

    }

    return render(request, 'home.html', context)





def profile(request):

    if request.method == 'POST':

        form = EmployeeForm(request.POST)
        
        if form.is_valid():
            employee= form.save(commit=False) 
            # post.author = request.user
            employee.save()           
            return HttpResponseRedirect('/form_saved_page/')
    
    else:
        form = EmployeeForm()

    return render(request, 'profile/employer_form.html', {'form': form})



