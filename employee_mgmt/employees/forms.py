from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.company = kwargs.pop('company', None)
        super().__init__(*args, **kwargs)

        if self.company:
            self.fields['team'].queryset = Team.objects.filter(company=self.company)
        elif self.instance.pk:
            self.fields['team'].queryset = Team.objects.filter(company=self.instance.company)
        else:
            self.fields['team'].queryset = Team.objects.none()

    class Meta:
        model = Employee
        exclude = ['company', 'created_by']
        widgets = {
            'date_of_joining': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'team':forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'identity_card_id':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'role':forms.TextInput(attrs={'class':'form-control'}),
            'photo':forms.FileInput(attrs={'class':'form-control'}),
            'blood_group':forms.Select(attrs={'class': 'form-control'}),
            'status':forms.Select(attrs={'class': 'form-control'}),

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
