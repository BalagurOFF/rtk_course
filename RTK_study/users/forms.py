from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm, \
    SetPasswordForm
from django.contrib.auth.models import Group
from django_select2.forms import Select2MultipleWidget


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class AdminRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'groups']
        labels = {
            'username': 'Логин',
            'password1': 'Пароль',
            'password2': 'Повторите пароль',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'groups': 'Группы пользователя',
        }
        widgets = {
            'username': forms.TextInput(attrs={'required': True}),
            'password1': forms.PasswordInput(attrs={'required': True}),
            'password2': forms.PasswordInput(attrs={'required': True}),
            'first_name': forms.TextInput(attrs={'required': True, 'title': 'Имя'}),
            'last_name': forms.TextInput(attrs={'required': False, 'title': 'Фамилия'}),
            'email': forms.TextInput(attrs={'required': False, 'title': 'Адрес электронной почты'}),
            'groups': Select2MultipleWidget(),
        }


class RegistrationForm(AdminRegistrationForm):
    class Meta(AdminRegistrationForm.Meta):
        exclude = ['groups']


class AdminCustumUserChangeForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'groups']
        labels = {
            'username': 'Имя пользователя',
            'email': 'Email',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'groups': 'Группы пользователя',
        }
        widgets = {
            'username': forms.TextInput(),
            'email': forms.TextInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'groups': Select2MultipleWidget(),
        }


class CustumUserChangeForm(AdminCustumUserChangeForm):
    class Meta(AdminCustumUserChangeForm.Meta):
        exclude = ['groups']
        widgets = {
            'username': forms.TextInput(attrs={'readonly': True}),
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'permissions']
        labels = {
            'name': 'Имя группы',
            'permissions': 'Права доступа',
        }
        widgets = {
            'name': forms.TextInput(),
            'permissions': Select2MultipleWidget(),
        }