from django import forms
from main.models import NewsModel, RegionModel, NewsTopicsModel


class AddNewsForm(forms.ModelForm):
    region = forms.ModelChoiceField(
        queryset=RegionModel.objects.all(),
        to_field_name='id',
        label='Регион',
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Выберите регион',
    )
    topicnews = forms.ModelChoiceField(
        queryset=NewsTopicsModel.objects.all(),
        to_field_name='id',
        label='Тематика новостей',
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Выберите тематику новостей',
    )

    class Meta:
        model = NewsModel
        fields = ['name', 'mainImage', 'description', 'region', 'topicnews']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mainImage': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
        }

        labels = {
            'name': 'Название',
            'mainImage': 'Основное изображение',
            'description': 'Текст новости',
        }


class RegionForm(forms.ModelForm):
    class Meta:
        model = RegionModel
        fields = ['description']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class NewsTopicsForm(forms.ModelForm):
    class Meta:
        model = NewsTopicsModel
        fields = ['description']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
