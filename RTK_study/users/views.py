from django.contrib.auth import logout, authenticate, login, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import PasswordChangeForm, AdminPasswordChangeForm
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import Group, Permission

# from django.contrib.auth.forms import *


User = get_user_model()


def registration(request):
    if request.method == 'POST':
        group_reader, create_group = Group.objects.get_or_create(name="Readers")
        if create_group:
            edit_profile = Permission.objects.get(codename="edit_profile")
            add_comments = Permission.objects.get(codename="add_comments")
            group_reader.permissions.add(edit_profile, add_comments)
            group_reader.save()
        if request.user.is_authenticated:
            if request.user.has_perm('user.user_administration'):
                form = AdminRegistrationForm(request.POST)
            else:
                return render(request, '403.html')
        else:
            form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 == password2:
                user = form.save()
                form.save_m2m()
                user.groups.add(group_reader)
                if request.user.is_authenticated and request.user.has_perm('user.user_administration'):
                    return redirect('users:listusers', permanent=True)
                else:
                    login(request, user)
                    return redirect('users:profile', permanent=True)
    else:
        if request.user.is_authenticated and request.user.has_perm('user.user_administration'):
            form = AdminRegistrationForm()
        else:
            form = RegistrationForm()
    return render(request, 'users/registration.html', {'form': form})


@permission_required('users.edit_profile', raise_exception=True)
def profile(request, id=None):
    if request.method == 'POST':
        if id is not None and request.user.has_perm('users.user_administration'):
            instance = User.objects.get(pk=id)
            form = AdminCustumUserChangeForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('users:listusers', permanent=True)
        else:
            instance = request.user
            form = CustumUserChangeForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('users:profile', permanent=True)
    else:
        if id is not None and request.user.has_perm('users.user_administration'):
            instance = User.objects.get(pk=id)
            form = AdminCustumUserChangeForm(instance=instance)
        else:
            instance = request.user
            form = CustumUserChangeForm(instance=instance)

    return render(request, 'users/profile.html', {'form': form, 'customer': instance})


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


@permission_required('users.edit_profile', raise_exception=True)
def reset_password(request, id=None):

    if request.method == "POST":
        if id is not None and request.user.has_perm('users.user_administration'):
            customer = User.objects.get(pk=id)
            form = AdminPasswordChangeForm(user=customer, data=request.POST)
            if form.is_valid():
                form.save()
        else:
            customer = request.user
            form = PasswordChangeForm(user=customer, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
    else:
        if id is not None and request.user.has_perm('users.user_administration'):
            customer = User.objects.get(pk=id)
            form = AdminPasswordChangeForm(user=customer)
        else:
            customer = request.user
            form = PasswordChangeForm(user=customer)
    return render(request, 'users/resetpassword.html', {'form': form, 'customer': customer})


@permission_required('users.user_administration', raise_exception=True)
def listusers(request):
    customers = User.objects.all().order_by('last_name')
    context = {
        'customers': customers,
    }
    return render(request, 'users/listusers.html', context)


@login_required()
def removeuser(request, id=None):
    if id is not None:
        if (id == request.user.id and request.user.has_perm('users.edit_profile')) or request.user.has_perm('users.user_administration'):
            User.objects.filter(id=id).update(is_active=False)
    if request.user.has_perm('users.user_administration'):
        return redirect('users:listusers', permanent=True)
    else:
        return redirect('main:news', permanent=True)


@permission_required('auth.change_group', raise_exception=True)
def listgroups(request):
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'users/listgroups.html', context)


@permission_required('auth.change_group', raise_exception=True)
def addgroup(request, id=None):
    if request.method == 'POST':
        if id is not None:
            instance = Group.objects.get(pk=id)
            form = GroupForm(request.POST, instance=instance)
        else:
            form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:listgroups', permanent=True)
    context = {}
    if id is not None:
        instance = Group.objects.get(pk=id)
        form = GroupForm(instance=instance)
        context['group'] = instance
    else:
        form = GroupForm()
    context['form'] = form
    return render(request, 'users/addgroup.html', context)


@permission_required('auth.change_group', raise_exception=True)
def removegroup(request, id=None):
    if id is not None:
        entry = Group.objects.filter(id=id)
        entry.delete()
    return redirect('users:listgroups', permanent=True)
