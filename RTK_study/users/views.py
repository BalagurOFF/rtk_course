from django.contrib.auth import logout
from django.shortcuts import render, redirect
from . import forms


def registration(request):
    form = forms.RegistrationForm()
    return render(request, 'users/registration.html', {'form': form})


def profile(request):
    form = forms.CustumUserChangeForm()
    return render(request, 'users/profile.html', {'form': form})


def login_user(request):
    form = forms.LoginUserForm()
    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('main:news', permanent=True)


def reset_password(request):
    form = forms.CustomPasswordChangeForm()
    return render(request, 'users/resetpassword.html', {'form': form})
