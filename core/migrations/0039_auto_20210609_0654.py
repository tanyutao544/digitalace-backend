# Generated by Django 3.2.3 on 2021-06-09 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20210609_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(blank=True, choices=[('PD', 'Paid'), ('UPD', 'Unpaid')], default='UPD', max_length=3),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(blank=True, choices=[('CP', 'Completed'), ('PD', 'Pending'), ('CC', 'Cancelled')], default='PD', max_length=3),
        ),
        migrations.AlterField(
            model_name='receive',
            name='status',
            field=models.CharField(blank=True, choices=[('PD', 'Paid'), ('UPD', 'Unpaid')], default='UPD', max_length=3),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='status',
            field=models.CharField(blank=True, choices=[('CP', 'Completed'), ('PD', 'Pending'), ('CC', 'Cancelled')], default='PD', max_length=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
