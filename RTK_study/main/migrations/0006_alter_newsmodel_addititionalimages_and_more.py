# Generated by Django 4.2.7 on 2023-11-16 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_newsmodel_addititionalimages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='addititionalImages',
            field=models.ImageField(max_length=1000, upload_to='news/%Y%m%d-%H%M/'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='mainImage',
            field=models.ImageField(max_length=200, upload_to='news/%Y%m%d-%H%M/'),
        ),
    ]