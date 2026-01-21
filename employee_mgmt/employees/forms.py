from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'name',
            'identity_card_id',
            'phone',
            'email',
            'team',
            'role',
            'photo',
            'blood_group',
            'date_of_joining',
            'status'
        ]
        widgets = {
            'date_of_joining': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'identity_card_id': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'team': forms.Select(attrs={'class':'form-control'}),
            'role': forms.TextInput(attrs={'class':'form-control'}),
            'photo': forms.FileInput(attrs={'class':'form-control'}),
            'blood_group': forms.Select(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
        }
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'})
        }
        
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['company', 'name']
        widgets = {
            'company': forms.Select(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'})
        }
class EmployeeWithUserForm(EmployeeForm):
    create_login = forms.BooleanField(
        required=False,
        label='Create system login for this employee'
    )
