from django.forms import ModelForm
from main_app.models import Employee

class EmployeeForm(ModelForm):
    
    class Meta:
        model = Employee
        exclude = ['is_active',] # '__all__'