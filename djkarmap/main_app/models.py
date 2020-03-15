from django.contrib.gis.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

from main_app.choices import GENDER_CHOICES, EDUCATION_CHOICES


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
    # phoneNumber = == >
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=20, blank=True, null=True)

    birth_date = models.DateField(blank=True, null=True)
    education = models.CharField(
        max_length=25,
        blank=True,
        choices=EDUCATION_CHOICES,
    )
    thumb = models.ImageField(upload_to='employee/thumb', blank=True)
    is_active = models.BooleanField(default=True)
    last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    image = models.ImageField(default='default.png',
                              blank=True, upload_to='employee')

    location = models.PointField(srid=4326, blank=True, null=True)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        from main_app.utils import generate_thumbnail
        self.thumb = generate_thumbnail(self.image)
        super(Employee, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        from main_app.utils import delete_from_s3
        delete_from_s3([self.image, self.thumb])
        super(Employee, self).delete(*args, **kwargs)


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
