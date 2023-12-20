from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm, \
    SetPasswordForm
from django.contrib.auth.models import Group
from django.core.validators import MinLengthValidator
from django_select2.forms import Select2MultipleWidget


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class AdminRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'required': True, 'title': 'Имя'}),
                                 validators=[MinLengthValidator(2, 'Слишком короткое имя')])
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'required': False, 'title': 'Фамилия'}),
                                validators=[MinLengthValidator(2, 'Слишком короткая фамилия')])

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'groups']
        labels = {
            'username': 'Логин',
            'password1': 'Пароль',
            'password2': 'Повторите пароль',
            'email': 'Email',
            'groups': 'Группы пользователя',
        }
        widgets = {
            'username': forms.TextInput(attrs={'required': True}),
            'password1': forms.PasswordInput(attrs={'required': True}),
            'password2': forms.PasswordInput(attrs={'required': True}),
            'email': forms.TextInput(attrs={'required': False, 'title': 'Адрес электронной почты'}),
            'groups': Select2MultipleWidget(),
        }

    field_order = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'groups']


class RegistrationForm(AdminRegistrationForm):
    class Meta(AdminRegistrationForm.Meta):
        exclude = ['groups']


class AdminCustumUserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active', 'groups']
        labels = {
            'username': 'Имя пользователя',
            'email': 'Email',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'is_active': 'Активный пользователь',
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
        exclude = ['is_active', 'groups']
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
