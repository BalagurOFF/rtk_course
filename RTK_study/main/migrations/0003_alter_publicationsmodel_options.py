# Generated by Django 4.1.10 on 2023-12-12 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publicationsmodel',
            options={'default_permissions': (), 'permissions': [('main_publications_editor', 'Can edit the publications of any author'), ('publications_editor', 'Can add, edit and delete only his own publications')], 'verbose_name_plural': 'Публикации'},
        ),
    ]
