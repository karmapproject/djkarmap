from django.contrib.gis import admin




from .models import JobGroup, Employee, Employer, Job, JobOrder

admin.site.register(JobGroup)
admin.site.register(Employer)
admin.site.register(Job)
admin.site.register(JobOrder)


@admin.register(Employee)
class EmployeeAdmin(admin.OSMGeoAdmin):
    list_display = ('user', 'gender', 'birth_date', 'education', 'is_active',)