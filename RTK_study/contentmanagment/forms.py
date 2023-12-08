from django import forms
from main.models import NewsModel, TagsModel
from django_select2.forms import Select2MultipleWidget, Select2Widget


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
    image_field = MultipleFileField(label = 'Медиа-материалы')

    class Meta:
        model = NewsModel
        fields = ['name', 'mainImage', 'description', 'tags', 'show_news']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mainImage': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'tags': Select2MultipleWidget(),
            'show_news': forms.CheckboxInput()
        }

        labels = {
            'name': 'Название',
            'mainImage': 'Основное изображение',
            'description': 'Текст новости',
            'tags': 'Тэги новостей',
            'show_news': 'Отображать новость'
        }


class TagsForm(forms.ModelForm):
    class Meta:
        model = TagsModel
        fields = ['description']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
