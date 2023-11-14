from django.contrib.auth import logout, authenticate, login, get_user_model
from django.shortcuts import render, redirect
from . import forms
#from django.contrib.auth.forms import *


User = get_user_model()
def registration(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 == password2:
                user = form.save()

                login(request, user)
                return redirect('users:profile')
    else:
        form = forms.RegistrationForm()
    return render(request, 'users/registration.html', {'form': form})


def profile(request):
    form = forms.CustumUserChangeForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = forms.LoginUserForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect('main:news', permanent=True)
    else:
        form = forms.LoginUserForm()
    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('main:news', permanent=True)


def reset_password(request):
    form = forms.CustomPasswordChangeForm()
    return render(request, 'users/resetpassword.html', {'form': form})
