from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_required
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from employees.models import Employee, Company
from .forms import *
from .models import *

User = get_user_model()

@login_required
def dashboard(request):

    feather = Company.objects.filter(name__iexact="Feather").first()
    ondezx = Company.objects.filter(name__iexact="Ondezx").first()

    feather_count = Employee.objects.filter(company=feather).count() if feather else 0
    ondezx_count = Employee.objects.filter(company=ondezx).count() if ondezx else 0

    total_employees = Employee.objects.count()
    total_users = User.objects.filter(is_active=True).count()

    active_employees = Employee.objects.filter(status='active').count()
    resigned_employees = Employee.objects.filter(status='resigned').count()

    context = {
        'feather_count': feather_count,
        'ondezx_count': ondezx_count,
        'total_employees': total_employees,
        'total_users': total_users,
        'active_employees': active_employees,
        'resigned_employees': resigned_employees,
    }

    return render(request, 'accounts/dashboard.html', context)


@admin_required
def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('dashboard')
    else:
        form = UserCreateForm()

    return render(request, 'accounts/create_user.html', {'form': form})

@login_required
@admin_required
def user_list(request):
    users = CustomUser.objects.all().order_by('username')
    return render(request, 'accounts/user_list.html', {'users': users})

@admin_required
def edit_user(request, user_id):
    user_obj = get_object_or_404(CustomUser, id=user_id)

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user_obj)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserEditForm(instance=user_obj)

    return render(request, 'accounts/edit_user.html', {
        'form': form,
        'user_obj': user_obj
    })

@admin_required
def delete_user(request, user_id):
    user_obj = get_object_or_404(CustomUser, id=user_id)

    # prevent admin deleting himself
    if user_obj == request.user:
        return redirect('user_list')

    if request.method == 'POST':
        user_obj.delete()
        return redirect('user_list')

    return render(request, 'accounts/delete_user.html', {
        'user_obj': user_obj
    })
