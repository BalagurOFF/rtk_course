from django.contrib.auth import logout, authenticate, login, get_user_model, update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import RegistrationForm, CustumUserChangeForm, LoginUserForm, CustomPasswordChangeForm

#from django.contrib.auth.forms import *


User = get_user_model()
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 == password2:
                user = form.save()

                login(request, user)
                return redirect('users:profile')
    else:
        form = RegistrationForm()
    return render(request, 'users/registration.html', {'form': form})


def profile(request):
    form = CustumUserChangeForm(instance=request.user)
    if request.method == 'POST':
        print(request.POST)
        form = CustumUserChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile', permanent=True)
        else:
            print('Форма не валидна')
    return render(request, 'users/profile.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect('main:news', permanent=True)
    else:
        form = LoginUserForm()
    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('main:news', permanent=True)


def reset_password(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'users/resetpassword.html', {'form': form})
