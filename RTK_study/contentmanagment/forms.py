from django import forms
from main.models import NewsModel, RegionModel, NewsTopicsModel


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


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
#    addititionalImages = MultipleFileField(label='Дополнительные материалы')

    class Meta:
        model = NewsModel
        fields = ['name', 'mainImage', 'description', 'region', 'topicnews']#, 'addititionalImages']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mainImage': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }

        labels = {
            'name': 'Название',
            'mainImage': 'Основное изображение',
            'description': 'Текст новости',
        }

