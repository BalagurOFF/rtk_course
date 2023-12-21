from django import forms
from django.urls import reverse_lazy
from django_addanother.widgets import AddAnotherWidgetWrapper
from main.models import PublicationsModel, TagsModel, ImagesModel
from django_select2.forms import Select2MultipleWidget
from django.forms.models import inlineformset_factory
from string import Template
from django.utils.safestring import mark_safe
from django.conf import settings
from django_addanother.contrib.select2 import Select2AddAnother


class ImagePreviewWidget(forms.widgets.FileInput):
    def render(self, name, value, attrs=None, **kwargs):
        input_html = super().render(name, value, attrs=None, **kwargs)
        img_html = mark_safe(f'<br>На данный момент: <img src="{settings.MEDIA_URL}{value}" width="60"/>')
        if value:
            return f'{input_html}{img_html}'
        else:
            return f'{input_html}'

class AddPublicationsForm(forms.ModelForm):
    #image_field = MultipleFileField(label = 'Медиа-материалы')

    class Meta:
        model = PublicationsModel
        fields = ['title', 'text', 'tags', 'show_news']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': '10'}),
            'tags': Select2MultipleWidget(attrs={'class': 'select2'}),
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
        widgets = {
            'image': ImagePreviewWidget,
        }


AddImageFormset = inlineformset_factory(PublicationsModel, ImagesModel, form=ImageForm, fields=['image', 'description'], extra=0)
