from django.contrib import admin
from .models import *

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company')
    list_filter = ('company',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'company',
        'team',
        'status',
        'date_of_joining'
    )
    list_filter = ('company', 'status')
    search_fields = ('name', 'email', 'identity_card_id')