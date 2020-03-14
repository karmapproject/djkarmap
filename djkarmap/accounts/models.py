from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    EMPLOYEE = 'KJ'
    EMPLOYER = 'KF'
    USER_TYPE_CHOICES = [
        (EMPLOYEE, 'کارجو'),
        (EMPLOYER, 'کارفرما'),
    ]

    user_type = models.CharField(choices=USER_TYPE_CHOICES, default=EMPLOYEE, max_length=10)

    def __str__(self):
        return self.username