from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm, \
    SetPasswordForm
from django_select2.forms import Select2MultipleWidget


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Логин',
            'password1': 'Пароль',
            'password2': 'Повторите пароль',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
        }
        widgets = {
            'username': forms.TextInput(attrs={'required': True}),
            'password1': forms.PasswordInput(attrs={'required': True}),
            'password2': forms.PasswordInput(attrs={'required': True}),
            'first_name': forms.TextInput(attrs={'required': True}),
            'last_name': forms.TextInput(attrs={'required': False}),
            'email': forms.TextInput(attrs={'required': False}),
        }


class AdminRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name','email', 'groups']
        labels = {
            'username': 'Логин',
            'password1': 'Пароль',
            'password2': 'Повторите пароль',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'groups': 'Группы пользователя'
        }
        widgets = {
            'username': forms.TextInput(attrs={'required': True}),
            'password1': forms.PasswordInput(attrs={'required': True}),
            'password2': forms.PasswordInput(attrs={'required': True}),
            'first_name': forms.TextInput(attrs={'required': True}),
            'last_name': forms.TextInput(attrs={'required': False}),
            'email': forms.TextInput(attrs={'required': False}),
            'groups': Select2MultipleWidget(),
        }


class CustumUserChangeForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'username': 'Имя пользователя',
            'email': 'Email',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        },
        widgets = {
            'username': forms.TextInput(attrs={'readonly': True}),
        }


class AdminCustumUserChangeForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'description', 'groups']
        labels = {
            'username': 'Имя пользователя',
            'email': 'Email',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'description': 'Занимаемая должность',
            'groups': 'Группы пользователя',
        },
        widgets = {
            'username': forms.TextInput(attrs={'readonly': True}),
            'groups': Select2MultipleWidget(),
        }


class CustomPasswordChangeForm(SetPasswordForm):
#    old_password = forms.CharField(label='Текущий пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'requared': True}))
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'requared': True}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control', 'requared': True}))
    class Meta:
        model = get_user_model()
#        labels = {
#            'old_password': 'Текущий пароль',
#            'new_password1': 'Новый пароль',
#            'new_password2': 'Повторите новый пароль',
#        },
