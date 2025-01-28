# Generated by Django 5.1.5 on 2025-01-23 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_rename_installaion_category_installationcategory_installation_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalinstallation',
            name='completed',
            field=models.BooleanField(default=True, verbose_name='Completada'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalinstallation',
            name='delayed',
            field=models.BooleanField(default=True, verbose_name='Demorada'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installation',
            name='completed',
            field=models.BooleanField(default=True, verbose_name='Completada'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installation',
            name='delayed',
            field=models.BooleanField(default=True, verbose_name='Demorada'),
            preserve_default=False,
        ),
    ]
