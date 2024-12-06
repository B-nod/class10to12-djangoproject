from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . forms import *
# Create your views here.

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password = data['password'])

            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('/admins')
                else:
                    return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid username or password !')
            return render(request, 'user/login.html', {'form':form})
        
    context = {
        'form':LoginForm
    }
    return render(request, 'user/login.html', context)

def logout_user(request):

    logout(request)
    return redirect('/users/login')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'User register successfully !')
            return redirect('/user/register')
        else:
            messages.add_message(request,  messages.ERROR, 'Error occure')
            return render(request, 'user/register.html', {'form':form})
            
    context = {
        'form':UserCreationForm
    }
    
    return render(request, 'user/register.html', context)
