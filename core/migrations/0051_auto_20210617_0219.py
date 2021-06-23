# Generated by Django 3.2.3 on 2021-06-17 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_auto_20210616_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designation',
            name='company',
        ),
        migrations.AddField(
            model_name='designation',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.department'),
            preserve_default=False,
        ),
    ]