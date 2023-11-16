from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegistrationForm(UserCreationForm):
#    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
#    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'username', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'required': True}),
            'username': forms.TextInput(attrs={'required': True}),
            'password1': forms.PasswordInput(attrs={'required': True}),
            'password2': forms.PasswordInput(attrs={'required': True}),
        }


class CustumUserChangeForm(forms.ModelForm):
#    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control', 'disabled': True}))
#    email = forms.CharField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
#    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
#    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
#    description = forms.CharField(label='Должность', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'description']
        labels = {
            'username': 'Имя пользователя',
            'email': 'Email',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'description': 'Занимаемая должность'
        },
        widgets = {
            'username': forms.TextInput(attrs={'readonly': True}),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Текущий пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'requared': True}))
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'requared': True}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control', 'requared': True}))
    class Meta:
        model = get_user_model()
#        labels = {
#            'old_password': 'Текущий пароль',
#            'new_password1': 'Новый пароль',
#            'new_password2': 'Повторите новый пароль',
#        },
