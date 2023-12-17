from django import forms
from main.models import PublicationsModel, TagsModel, ImagesModel
from django_select2.forms import Select2MultipleWidget, Select2Widget
from django.forms.models import inlineformset_factory


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


class AddPublicationsForm(forms.ModelForm):
    image_field = MultipleFileField(label = 'Медиа-материалы')

    class Meta:
        model = PublicationsModel
        fields = ['title', 'text', 'tags', 'show_news']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'tags': Select2MultipleWidget(),
            'show_news': forms.CheckboxInput()
        }

        labels = {
            'title': 'Название',
            'text': 'Текст новости',
            'tags': 'Тэги новостей',
            'show_news': 'Отображать новость'
        }
    field_order = ['title', 'image_field', 'text', 'tags', 'show_news']


class TagsForm(forms.ModelForm):
    class Meta:
        model = TagsModel
        fields = ['description']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImagesModel
        fields = ['image', 'description']
        labels = {
            'image': 'Изображение',
            'description': 'Описание',
        }


AddImageFormset = inlineformset_factory(PublicationsModel, ImagesModel, form=ImageForm, fields=['image', 'description'], extra=1)
