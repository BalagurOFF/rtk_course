# Generated by Django 4.2.7 on 2023-11-13 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsmodel',
            options={'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='newstopicsmodel',
            options={'verbose_name_plural': 'Тематики новостей'},
        ),
        migrations.AlterModelOptions(
            name='regionmodel',
            options={'verbose_name_plural': 'Регионы'},
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='description',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.CreateModel(
            name='NewsCommentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_comment', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(blank=True, max_length=1000)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.newsmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
