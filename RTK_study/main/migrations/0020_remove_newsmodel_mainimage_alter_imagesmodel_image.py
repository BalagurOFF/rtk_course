# Generated by Django 4.2.7 on 2023-12-08 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_imagesmodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsmodel',
            name='mainImage',
        ),
        migrations.AlterField(
            model_name='imagesmodel',
            name='image',
            field=models.ImageField(max_length=200, upload_to='news/%Y%m%d/'),
        ),
    ]
