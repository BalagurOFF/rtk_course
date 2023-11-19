from django.contrib.auth import logout, authenticate, login, get_user_model, update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect
from .forms import RegistrationForm, CustumUserChangeForm, LoginUserForm, CustomPasswordChangeForm, AdminUserChangeForm

# from django.contrib.auth.forms import *


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


def reset_password(request, id=None):
    if id == None:
        customer = request.user
    else:
        customer = User.objects.get(pk=id)
    if request.method == "POST":
        form = CustomPasswordChangeForm(user=customer, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        form = CustomPasswordChangeForm(user=customer)
    return render(request, 'users/resetpassword.html', {'form': form})


def listusers(request):
    customers = User.objects.all()
    context = {
        'customers': customers,
    }
    return render(request, 'users/listusers.html', context)


def userupdate(request, id=None):
    if id == None:
        form = RegistrationForm()
        context = {
            'form': form,
        }
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                password1 = form.cleaned_data.get('password1')
                password2 = form.cleaned_data.get('password2')
                if password1 == password2:
                    form.save()
            return redirect('users:listusers', permanent=True)
    else:
        form = UserChangeForm(instance=User.objects.get(pk=id))
        context = {
            'form': form,
            'customer': User.objects.get(pk=id),
        }
        if request.method == "POST":
            form = UserChangeForm(request.POST, instance=User.objects.get(pk=id))
            if form.is_valid():
                print(request.POST)
                try:
                    form.save
                except Exception as err:
                    print(err)
            else:
                print('Форма не валидна')
            return redirect('users:listusers', permanent=True)
    return render(request, 'users/userupdate.html', context)


def removeuser(request, id=None):
    if id != None:
        entry = User.objects.filter(id=id)
        entry.delete()
    return redirect('users:listusers', permanent=True)
