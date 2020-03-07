from django.contrib.gis import admin

from .models import JobGroup, Employee, Employer, Job, JobOrder

admin.site.register(JobGroup)
admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(Job)
admin.site.register(JobOrder)
