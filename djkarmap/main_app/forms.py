from django.forms import ModelForm
from main_app.models import Employee

class EmployeeForm(ModelForm):
    
    class Meta:
        model = Employee
        exclude = '__all__' # ['is_active', 'user__first_name',] # 