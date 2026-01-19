from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_required
from django.views.decorators.http import require_POST
from .forms import *
from .models import *


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


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
