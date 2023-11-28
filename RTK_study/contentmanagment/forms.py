from django import forms
from main.models import NewsModel, RegionModel, NewsTopicsModel
from django_select2 import forms as s2forms

#class RegionWidget(s2forms.ModelSelect2MultipleWidget):
#    search_fields = [
#        "description__icontains",
#    ]


#class TopicsWidget(s2forms.ModelSelect2MultipleWidget):
#    search_fields = [
#        "description__icontains",
#    ]


class AddNewsForm(forms.ModelForm):

    class Meta:
        model = NewsModel
        fields = ['name', 'mainImage', 'description', 'region', 'topicnews',]# 'show_news']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mainImage': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'region': forms.SelectMultiple(attrs={'class': 'select2'}),
            'topicnews': forms.SelectMultiple(attrs={'class': 'select2'}),
        }

        labels = {
            'name': 'Название',
            'mainImage': 'Основное изображение',
            'description': 'Текст новости',
            'region': 'Выберите регионы',
            'topicnews': 'Тематика новостей',
            #'show_news': 'Отображать новость'
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
