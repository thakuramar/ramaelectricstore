# Generated by Django 3.1.1 on 2021-02-08 15:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramaelectric', '0036_auto_20210208_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpage',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be in the format: 05999999999', regex='^(05)\\d{9}$')]),
        ),
    ]
