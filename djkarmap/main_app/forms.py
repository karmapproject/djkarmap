from django.contrib.gis import forms
from main_app.models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        exclude = ['is_active', 'user', 'thumb', ]
        widgets = {
            'birth_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'datepicker'}),
            'location': forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500, 'default_lat': 35.7, 'default_lon': 51.3}),
           
        }
