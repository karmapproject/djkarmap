from django.contrib.gis import admin

from .models import JobGroup, Job, Skil, Employee, Employer, JobOrder

admin.site.register(JobGroup)
admin.site.register(Job, admin.GeoModelAdmin)
admin.site.register(Skil)
admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(JobOrder)

