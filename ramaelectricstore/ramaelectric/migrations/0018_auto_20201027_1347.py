# Generated by Django 3.1.1 on 2020-10-27 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ramaelectric', '0017_auto_20201027_1343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='items',
            options={'get_latest_by': 'arrival_date'},
        ),
    ]