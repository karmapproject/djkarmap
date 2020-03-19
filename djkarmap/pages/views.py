
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point

from main_app.models import JobGroup, JobOrder, Employee
from main_app.forms import EmployeeForm



user_lon = 51.3
user_lat = 35.7
user_location = Point(user_lon, user_lat, srid=4326)



def home(request):
    latest_job_groups = JobGroup.objects.all()
    latest_job_order = JobOrder.objects.order_by('-created')[:5]    
  

    context = {
        'latest_job_group': latest_job_groups,
        'latest_job_order': latest_job_order,
       
    }

    return render(request, 'home.html', context)



nearest_jobs_order = JobOrder.objects.all()
# print(nearest_jobs_order)
# nearest_jobs_order = JobOrder.objects.annotate(distance=Distance('job__location',
#     user_location)).order_by('distance')[0:10]

def profile(request):
    if request.method == 'POST':      

        form = EmployeeForm(request.POST, request.FILES)
        
        if form.is_valid():            
            employee= form.save(commit=False)
            employee.user = request.user 
            # post.author = request.user
            employee.save()           
            # return HttpResponseRedirect('/form_saved_page/')
            # print(request.POST)
    
    else:
        form = EmployeeForm()

    return render(request, 'profile/profile.html', {'form': form, 'nearest_jobs_order': nearest_jobs_order})



