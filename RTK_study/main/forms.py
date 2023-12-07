from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import NewsCommentsModel, ContactModel


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


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['sender', 'contact', 'message']
        widgets = {
            'sender': forms.TextInput(),
            'contact': forms.TextInput(),
            'message': forms.Textarea(attrs={'rows': '5'}),
        }
        labels = {
            'sender': 'Представьтесь пожалуйста',
            'contact': 'Укажите данные, по которым можно с вами связаться',
            'message': 'Текст сообщения'
        }
