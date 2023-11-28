# Generated by Django 4.2.7 on 2023-11-28 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_newsmodel_region_newsmodel_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='region',
            field=models.ManyToManyField(blank=True, related_name='Регионы', to='main.regionmodel'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='topicnews',
            field=models.ManyToManyField(blank=True, related_name='Тематики', to='main.newstopicsmodel'),
        ),
    ]