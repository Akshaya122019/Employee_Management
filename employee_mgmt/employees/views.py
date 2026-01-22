from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_required
from .models import *
from .forms import *
from accounts.forms import UserCreateForm


@login_required
@admin_required
def add_employee(request, company_name):
    company = get_object_or_404(Company, name__iexact=company_name)

    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, company=company)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.company = company
            employee.created_by = request.user
            employee.save()
            return redirect('dashboard')
    else:
        form = EmployeeForm(company=company)

    return render(request, 'employees/add_employee.html', {
        'form': form,
        'company': company
    })


# @login_required
# def employee_list(request):
#     employees = Employee.objects.select_related('team', 'company')

#     status = request.GET.get('status')
#     if status in ['active', 'resigned']:
#         employees = employees.filter(status=status)

#     return render(request, 'employees/employee_list.html', {
#         'employees': employees
#     })

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'employees/company_list.html', {'companies': companies})


def company_employees(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    employees = Employee.objects.filter(company=company).select_related('team')

    status = request.GET.get('status')
    if status:
        employees = employees.filter(status=status)

    return render(request, 'employees/company_employees.html', {
        'company': company,
        'employees': employees
    })

@login_required
@admin_required
def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        form = EmployeeForm(
            request.POST,
            request.FILES,
            instance=employee
        )
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
        # filter teams by company
        form.fields['team'].queryset = Team.objects.filter(
            company=employee.company
        )

    return render(request, 'employees/edit_employee.html', {
        'form': form,
        'employee': employee
    })

@login_required
@admin_required
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        employee.status = 'resigned'
        employee.save()
        return redirect('employee_list')

    return render(request, 'employees/delete_employee.html', {
        'employee': employee
    })

@login_required
@admin_required
def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CompanyForm()

    return render(request, 'employees/add_company.html', {'form': form})

@login_required
@admin_required
def view_company(request):
    company = Company.objects.all()
    return render(request,"employees/view_company.html",{'company':company})

@login_required
@admin_required
def edit_company(request,pk):
    company=get_object_or_404(Company,pk=pk)
    if request.method == "POST":
        form = CompanyForm(request.POST,instance=company)
        if form.is_valid():
            form.save()
            return redirect('view_company')
    else:
        form = CompanyForm(instance=company)
    return render(request,"employees/edit_company.html",{'form':form})


@login_required
@admin_required
def company_delete(request,pk):
    detail=Company.objects.get(id=pk)
    detail.delete()
    return redirect('view_company')

@login_required
@admin_required
def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TeamForm()

    return render(request, 'employees/add_team.html', {'form': form})

@login_required
@admin_required
def view_team(request):
    team = Team.objects.all()
    return render(request,"employees/view_team.html",{'team':team})