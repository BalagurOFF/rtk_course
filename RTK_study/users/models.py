from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Admin = 'admin'
    Autor = 'autor'
    Reader = 'reader'
    work_status_choices = [
        (Admin, 'Администрация'),
        (Autor, 'Автор новостей'),
        (Reader, 'Читатель'),
    ]
    description = models.CharField(max_length=150, blank=True, verbose_name='Занимаемая должность',)
    work_status = models.CharField(max_length=10, choices=work_status_choices, default=Reader, verbose_name='Тип пользователя')
#    region = models.ForeignKey('RegionModel', on_delete=models.PROTECT)
