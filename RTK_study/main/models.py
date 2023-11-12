from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _


class RegionModel(models.Model):
    code = models.CharField(max_length=3, unique=True)
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.description

class NewsTopicsModel(models.Model):
    code = models.CharField(max_length=3, unique=True)
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = 'Тематики новостей'

    def __str__(self):
        return self.description


class NewsModel(models.Model):
    region = models.ForeignKey(RegionModel, on_delete=models.PROTECT)
    topicnews = models.ForeignKey(NewsTopicsModel, on_delete=models.PROTECT)
    autor = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    name = models.CharField(max_length=150, blank=True)
    mainImage = models.ImageField(upload_to="upload/%Y/%m/%d/", max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    date_pub = models.DateTimeField(auto_now=True)
    addititionalImages = models.ImageField(upload_to="upload/%Y/%m/%d/", max_length=200)

    class Meta:
        verbose_name_plural = 'Новости'
