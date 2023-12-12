from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    description = models.CharField(max_length=150, blank=True, verbose_name='Занимаемая должность',)


    class Meta:
        verbose_name_plural = 'Пользователи'
        default_permissions = ()
        permissions = [
            ('edit_profile', 'Сan change his profile data'),
            ('user_administration', 'Can add, change and delete user data')
        ]

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'id': self.id})
