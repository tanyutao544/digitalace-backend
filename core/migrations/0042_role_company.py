# Generated by Django 3.2.3 on 2021-06-12 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_remove_role_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.company'),
            preserve_default=False,
        ),
    ]