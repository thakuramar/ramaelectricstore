# Generated by Django 3.1.1 on 2020-10-27 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ramaelectric', '0018_auto_20201027_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='items',
            options={'get_latest_by': ['-arrival_date']},
        ),
    ]
