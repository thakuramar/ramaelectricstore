# Generated by Django 3.1.1 on 2020-10-28 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramaelectric', '0027_auto_20201028_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='arrival_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
