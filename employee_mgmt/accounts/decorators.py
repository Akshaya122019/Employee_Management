from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def admin_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.role != 'admin':
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper
