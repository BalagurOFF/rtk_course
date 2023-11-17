from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    description = models.CharField(max_length=150, blank=True, verbose_name='Занимаемая должность',)
