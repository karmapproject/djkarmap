from django.contrib.auth.models import User
from .models import JobGroup, Job, Skil, Employee, Employer, JobOrder


num_user = 5
User.objects.exclude(username='admin').delete()

for i in range(num_user):
    user = User.objects.create_user('username %s'%i, 'username%s@gmail.com'%i, 'User123456789')
    user.first_name = 'morteza %s'%i
    user.last_name = 'morteza %s'%i
    user.save()

