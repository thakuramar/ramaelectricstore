# Generated by Django 3.1.1 on 2020-12-10 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramaelectric', '0031_appointmentform_updated_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
