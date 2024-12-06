from django.shortcuts import render, redirect

def admin_only(view_fun):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return view_fun(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_function