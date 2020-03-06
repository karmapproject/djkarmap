from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from main_app.models import *


for i in range(5):
    user = User.objects.create_user(
        'username %s' % i, 'username%s@gmail.com' % i, 'User123456789')
    user.first_name = 'morteza %s' % i
    user.last_name = 'morteza %s' % i
    user.save()


for i in range(5):
    jobgroup = JobGroup(title="jobGroup%s" % i)
    jobgroup.save()


for i in range(5):
    x, y = 51.3, 35.7
    title = "jobTitle%s" % i
    location = Point(x + (i/100), y + (i/100))
    jobgroup = JobGroup.objects.all()[i]
    job_type = i
    description = "description related to job %s" % i
    job = Job(title=title, location=location, group=jobgroup,
              job_type=job_type, description=description)
    job.save()


for i in range(5):
    skil = Skil(title="Skill%s" %
                i, description="description related to job %s" % i)
    skil.save()


for i in range(5):
    user = User.objects.all()[i]
    skil = Skil.objects.all()[i]
    job1 = Job.objects.all()[i:5][1]
    job2 = Job.objects.all()[i:5][i]
    skil1 = Skil.objects.all()[i:5][1]
    skil2 = Skil.objects.all()[i:5][i]
    employe = Employee(user=user)
    employe.searchfor.add(job1, job2)
    employe.skils.add(skil, skil2)
    employe.save()
