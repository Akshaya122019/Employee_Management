from django.urls import path
from .views import *

urlpatterns = [
    path('add/<str:company_name>/', add_employee, name='add_employee'),
    path('company/add/', add_company, name='add_company'),
    path('team/add/', add_team, name='add_team'),
    path('employees/', company_list, name='company_list'),
    path('edit/<int:employee_id>/', edit_employee, name='employee_edit'),
    path('delete/<int:employee_id>/', delete_employee, name='employee_delete'),
    path('companies/', view_company, name='view_company'),
    path('company/edit/<int:pk>/', edit_company, name='edit_company'),
    path('company/delete/<int:pk>/', company_delete, name='company_delete'),
    path('teams/', view_team, name='view_team'),
    path("company/<int:company_id>/", company_employees, name="company_employees"),
    



]
