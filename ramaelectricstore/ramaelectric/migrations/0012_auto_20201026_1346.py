# Generated by Django 3.1.1 on 2020-10-26 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramaelectric', '0011_auto_20201026_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
