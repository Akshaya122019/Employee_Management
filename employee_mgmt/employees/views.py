from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_required
from .models import *
from .forms import *
from accounts.forms import UserCreateForm

@admin_required
def add_employee(request, company_name):
    company = get_object_or_404(Company, name__iexact=company_name)

    if request.method == 'POST':
        employee_form = EmployeeWithUserForm(request.POST, request.FILES)
        user_form = UserCreateForm(request.POST)

        if employee_form.is_valid():
            employee = employee_form.save(commit=False)
            employee.company = company
            employee.created_by = request.user

            # OPTIONAL LOGIN CREATION
            if employee_form.cleaned_data.get('create_login'):
                if user_form.is_valid():
                    user = user_form.save(commit=False)
                    user.set_password(user_form.cleaned_data['password'])
                    user.save()
                    employee.user = user
                else:
                    return render(request, 'employees/add_employee.html', {
                        'employee_form': employee_form,
                        'user_form': user_form,
                        'company': company
                    })

            employee.save()
            return redirect('employee_list')

    else:
        employee_form = EmployeeWithUserForm()
        user_form = UserCreateForm()

    return render(request, 'employees/add_employee.html', {
        'employee_form': employee_form,
        'user_form': user_form,
        'company': company
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
def employee_list(request):
    employees = Employee.objects.select_related('user', 'team', 'company')

    status = request.GET.get('status')
    if status in ['active', 'resigned']:
        employees = employees.filter(status=status)

    return render(request, 'employees/employee_list.html', {
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

