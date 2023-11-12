from django import forms
from main.models import NewsModel, RegionModel, NewsTopicsModel


class AddNewsForm(forms.ModelForm):
    region = forms.ModelChoiceField(
        queryset=RegionModel.objects.all(),
        to_field_name='code',
        label='Регион',
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Выберите регион',
    )
    topicnews = forms.ModelChoiceField(
        queryset=NewsTopicsModel.objects.all(),
        to_field_name='code',
        label='Тематика новостей',
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Выберите тематику новостей',
    )
    class Meta:
        model = NewsModel
        fields = ['name', 'mainImage', 'description', 'addititionalImages', 'region', 'topicnews']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mainImage': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'addititionalImages': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Название',
            'mainImage': 'Основное изображение',
            'description': 'Текст новости',
            'addititionalImages': 'Дополнительные материалы',
        }
