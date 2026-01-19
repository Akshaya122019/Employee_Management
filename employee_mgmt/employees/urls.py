from django.urls import path
from .views import *

urlpatterns = [
    path('add/<str:company_name>/', add_employee, name='add_employee'),
    path('company/add/', add_company, name='add_company'),
    path('team/add/', add_team, name='add_team'),
    path('list/', employee_list, name='employee_list'),
    path('edit/<int:employee_id>/', edit_employee, name='employee_edit'),
    path('delete/<int:employee_id>/', delete_employee, name='employee_delete'),

]
