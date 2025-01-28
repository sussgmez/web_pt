# Generated by Django 5.1.5 on 2025-01-27 01:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_remove_historicalinstallation_device_list_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(default='', verbose_name='Dirección'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='installation_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.installationcategory', verbose_name='Categoría'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='installation_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.installationtype', verbose_name='Tipo de instalación'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_1',
            field=models.CharField(default='', max_length=20, verbose_name='Teléfono 1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalcustomer',
            name='address',
            field=models.TextField(default='', verbose_name='Dirección'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalcustomer',
            name='installation_category',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='orders.installationcategory', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='historicalcustomer',
            name='phone_1',
            field=models.CharField(default='04123456789', max_length=20, verbose_name='Teléfono 1'),
            preserve_default=False,
        ),
    ]
