# Generated by Django 3.1.1 on 2020-10-25 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramaelectric', '0009_items_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
