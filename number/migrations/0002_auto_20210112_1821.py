# Generated by Django 3.1 on 2021-01-12 21:21

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('number', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='result_array',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(validators=[django.core.validators.MinValueValidator(-1000), django.core.validators.MaxValueValidator(1000)]), blank=True, null=True, size=None),
        ),
    ]
