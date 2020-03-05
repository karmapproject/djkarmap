from django.contrib.gis.db import models
from django.contrib.auth.models import User




class JobGroup(models.Model):
    title =  models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Job(models.Model):
    SRID = 4326
    JOB_TYPE = (
        (1, "تمام وقت"),
        (2, "پاره وقت"),
        (3, "پروژه‌ای"),
        (4, "کارآموزی"),
        (5, "توافقی"),
        (6, "سایر"),
    )

    title =  models.CharField(max_length=50)
    location = models.PointField(srid=SRID)
    group = models.ForeignKey(JobGroup, on_delete=models.CASCADE)
    job_type = models.PositiveSmallIntegerField(choices=JOB_TYPE)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Skil(models.Model):
    title = models.CharField(max_length=100)    
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name 


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    skils = models.ManyToManyField(Skil)
    searchfor = models.ManyToManyField(Job)

    def __str__(self):
        return self.user.name



class Employer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    searchfor = models.ManyToManyField(Job)

    def __str__(self):
        return self.user.name



class JobOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    searchfor = models.ManyToManyField(Job)

    def __str__(self):
        return self.user.name

