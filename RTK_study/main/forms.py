from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm



class AddNewsForm(forms.Form):
    name = forms.CharField(label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}))
    mainImage = forms.FileField(label='Основное изображение', widget = forms.FileInput(attrs={'class': 'form-control'}))
    newsText = forms.CharField(label='Текст новости', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    addititionalImages = forms.FileField(label='Дополнительное изображение', widget = forms.FileInput(attrs={'class': 'form-control'}))

