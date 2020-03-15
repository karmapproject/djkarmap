from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = get_user_model()
        fields =  ('username', 'user_type', 'first_name', 'last_name',) # 'email'




class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields =  ('username', 'email', 'user_type', ) 
