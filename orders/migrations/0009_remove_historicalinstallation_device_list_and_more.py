# Generated by Django 5.1.5 on 2025-01-23 19:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_remove_historicalinstallation_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalinstallation',
            name='device_list',
        ),
        migrations.RemoveField(
            model_name='historicalinstallation',
            name='installation_category',
        ),
        migrations.RemoveField(
            model_name='historicalinstallation',
            name='installation_type',
        ),
        migrations.RemoveField(
            model_name='installation',
            name='device_list',
        ),
        migrations.RemoveField(
            model_name='installation',
            name='installation_category',
        ),
        migrations.RemoveField(
            model_name='installation',
            name='installation_type',
        ),
        migrations.AddField(
            model_name='customer',
            name='device_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.devicelist', verbose_name='Equipos'),
        ),
        migrations.AddField(
            model_name='customer',
            name='installation_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.installationcategory', verbose_name='Categoría de instalación'),
        ),
        migrations.AddField(
            model_name='customer',
            name='installation_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.installationtype', verbose_name='Tipo de instalación'),
        ),
        migrations.AddField(
            model_name='historicalcustomer',
            name='device_list',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='orders.devicelist', verbose_name='Equipos'),
        ),
        migrations.AddField(
            model_name='historicalcustomer',
            name='installation_category',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='orders.installationcategory', verbose_name='Categoría de instalación'),
        ),
        migrations.AddField(
            model_name='historicalcustomer',
            name='installation_type',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='orders.installationtype', verbose_name='Tipo de instalación'),
        ),
    ]
