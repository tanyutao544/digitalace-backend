# Generated by Django 3.2.3 on 2021-06-06 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20210606_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconfig',
            name='language',
            field=models.CharField(blank=True, default='en', max_length=255),
        ),
        migrations.AddField(
            model_name='userconfig',
            name='theme',
            field=models.CharField(blank=True, default='light', max_length=255),
        ),
    ]