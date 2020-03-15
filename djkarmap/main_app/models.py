from django.contrib.gis.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


class JobGroup(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):
    """ 
        This means that a given user can be the author of many different blog posts
        but not the other way around.
    """
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    location = models.PointField(srid=4326, blank=True, null=True)
    gender = models.CharField(choices=(
        ('male', 'مرد'), ('female', 'زن'),), max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    image = models.ImageField(default='', blank=True, upload_to='employee')

    def __str__(self):
        return self.user.email


class Employer(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    location = models.PointField(srid=4326, blank=True, null=True)
    employer_type = models.CharField(choices=(
        ('person', 'Person'), ('company', 'Company'),), max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.user.email


class Job(models.Model):
    JOB_TYPE = (
        (1, "تمام وقت"),
        (2, "پاره وقت"),
        (3, "پروژه‌ای"),
        (4, "کارآموزی"),
        (5, "توافقی"),
        (6, "سایر"),
    )
    title = models.CharField(max_length=100)
    group = models.ForeignKey(JobGroup, on_delete=models.CASCADE)
    location = models.PointField(srid=4326, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('job_detail', args=[f'{self.id}'])


class JobOrder(models.Model):    
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f'{self.user}: {self.created.__str__()}'