from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class UserProfile(AbstractUser):     
    
    user_type = models.CharField(
        choices=(('Employer', 'Employer'), ('Employee', 'Employee'),), max_length=50)    
    last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)


    def __str__(self):
        return 'Profile of user: {}'.format(self.username)


