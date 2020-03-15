from django import forms
from main_app.models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        exclude = ['is_active', 'user', 'thumb', ]
        widgets = {
            'birth_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }
