# Generated by Django 3.2.3 on 2021-06-06 17:17

import core.models.maintenance
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20210606_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=core.models.maintenance.product_image_file_path),
        ),
    ]