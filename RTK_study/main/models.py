from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


User = get_user_model()
class TagsModel(models.Model):
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = 'Тэги новостей'

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('contentmanagment:tags', kwargs={'id': self.id})


class NewsModel(models.Model):
    tags = models.ManyToManyField('TagsModel',blank=True, related_name='Тэги')
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    date_pub = models.DateTimeField(auto_now=True)
    show_news = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:newsFull', kwargs={'id': self.id})


class NewsCommentsModel(models.Model):
    date_comment = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    news = models.ForeignKey(NewsModel, on_delete=models.CASCADE)
    text = models.TextField(max_length=10000, blank=True)
    show_comment = models.BooleanField(default=True)


class ContactModel(models.Model):
    date_message = models.DateTimeField(auto_now=True)
    sender = models.TextField(max_length=100, blank=False)
    contact = models.TextField(max_length=100, blank=False)
    message = models.TextField(max_length=10000, blank=False)

    class Meta:
        verbose_name_plural = 'Сообщения для администрации'

    def __str__(self):
        return self.contact

    def get_absolute_url(self):
        return reverse('main:messagedetail', kwargs={"pk": self.pk})


class ImagesModel(models.Model):
    news = models.ForeignKey(NewsModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/%Y%m%d/', max_length=200)
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'Медиа-материалы'

    def __str__(self):
        return self.description
