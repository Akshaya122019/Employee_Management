from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'name',
            'identity_card_id',
            'phone',
            'team',
            'role',
            'photo',
            'blood_group',
            'date_of_joining',
            'status'
        ]
        widgets = {
            'date_of_joining': forms.DateInput(attrs={'type': 'date'})
        }
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']
        
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['company', 'name']
class EmployeeWithUserForm(EmployeeForm):
    create_login = forms.BooleanField(
        required=False,
        label='Create system login for this employee'
    )
