# Generated by Django 3.1.1 on 2020-10-25 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramaelectric', '0008_auto_20201025_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/% Y/% m/% d/'),
        ),
    ]