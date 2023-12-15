from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

User = get_user_model()


class TagsModel(models.Model):
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = 'Тэги публикаций'
        default_permissions = ()
        permissions = [
            ('tags_editor', 'Can edit the tags')
        ]

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('contentmanagment:tags', kwargs={'id': self.id})


class PublicationsModel(models.Model):
    tags = models.ManyToManyField('TagsModel', blank=True, related_name='Тэги')
    autor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='autor')
    title = models.CharField(max_length=150, blank=True)
    text = models.TextField(blank=True)
    date_pub = models.DateTimeField(null=True)
    show_news = models.BooleanField(default=True)
    editor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='editor')
    date_edit = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Публикации'
        default_permissions = ()
        permissions = [
            ('main_publications_editor', 'Can edit the publications of any author'),
            ('publications_editor', 'Can add, edit and delete only his own publications')
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:newsFull', kwargs={'id': self.id})


class PublicationsCommentsModel(models.Model):
    date_comment = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    news = models.ForeignKey(PublicationsModel, on_delete=models.CASCADE)
    text = models.TextField(max_length=10000, blank=True)
    show_comment = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Комментарии'
        default_permissions = ()
        permissions = [
            ('moderation', 'Can set the status of the comments'),
            ('add_comments', 'Can add comments')
        ]


class ContactModel(models.Model):
    date_message = models.DateTimeField(auto_now=True)
    sender = models.TextField(max_length=100, blank=False)
    contact = models.TextField(max_length=100, blank=False)
    message = models.TextField(max_length=10000, blank=False)

    class Meta:
        verbose_name_plural = 'Сообщения для администрации'
        default_permissions = ()
        permissions = [
            ('view_messages', 'Can view messages'),
        ]

    def __str__(self):
        return self.contact

    def get_absolute_url(self):
        return reverse('main:messagedetail', kwargs={"pk": self.pk})


class ImagesModel(models.Model):
    news = models.ForeignKey(PublicationsModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/%Y%m%d/', max_length=200)
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'Медиа-материалы'
        default_permissions = ()
        permissions = [
            ('image_editor', 'Can add or delete images for publication'),
        ]

    def __str__(self):
        return self.description
