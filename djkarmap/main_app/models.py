from django.contrib.gis.db import models
from django.contrib.auth.models import User


class JobGroup(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Skil(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.PointField(srid=4326, blank=True, null=True)
    gender = models.CharField(choices=(
        ('male', 'Male'), ('female', 'Female'),), max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.PointField(srid=4326, blank=True, null=True)
    employer_type = models.CharField(choices=(
        ('person', 'Person'), ('company', 'Company'),), max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.user.username


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
