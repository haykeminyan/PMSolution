# Generated by Django 4.1.2 on 2022-11-13 22:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internal',
            name='percent',
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(10.0),
                ],
            ),
        ),
        migrations.AlterField(
            model_name='internal',
            name='quantity',
            field=models.IntegerField(
                blank=True,
                help_text='Armencho mihat gri sti',
                null=True,
                validators=[django.core.validators.MinValueValidator(1.0)],
            ),
        ),
        migrations.AlterField(
            model_name='internal',
            name='quantity_after_percent',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
