# Generated by Django 3.2.3 on 2021-06-08 17:17

import core.models.maintenance
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_20210608_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, upload_to=core.models.maintenance.customer_image_file_path),
        ),
        migrations.AddField(
            model_name='supplier',
            name='image',
            field=models.ImageField(blank=True, upload_to=core.models.maintenance.supplier_image_file_path),
        ),
    ]