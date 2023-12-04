from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm

from .models import NewsCommentsModel


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = NewsCommentsModel
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }

        labels = {
            'text': 'Текст комментария',
        }


class ContactForm(forms.Form):
    name = forms.CharField(label='Представьтесь пожалуйста', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email для обратной связи', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label='Текст сообщения', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

