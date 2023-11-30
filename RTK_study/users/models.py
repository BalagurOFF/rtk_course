from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    description = models.CharField(max_length=150, blank=True, verbose_name='Занимаемая должность',)

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'id': self.id})
