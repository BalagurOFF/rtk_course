from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


User = get_user_model()
class RegionModel(models.Model):
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('contentmanagment:regions', kwargs={'id': self.id})


class NewsTopicsModel(models.Model):
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = 'Тематики новостей'

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('contentmanagment:topics', kwargs={'id': self.id})


class NewsModel(models.Model):
    region = models.ForeignKey(RegionModel, on_delete=models.PROTECT)
    topicnews = models.ForeignKey(NewsTopicsModel, on_delete=models.PROTECT)
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=150, blank=True)
    mainImage = models.ImageField(upload_to='news/%Y%m%d-%H%M/', max_length=200)
    description = models.TextField(blank=True)
    date_pub = models.DateTimeField(auto_now=True)
    show_news = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):
        return reverse('main:newsFull', kwargs={'id': self.id})


class NewsCommentsModel(models.Model):
    date_comment = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    news = models.ForeignKey(NewsModel, on_delete=models.CASCADE)
    text = models.TextField(max_length=10000, blank=True)
    show_comment = models.BooleanField(default=True)
