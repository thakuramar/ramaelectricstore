# Generated by Django 3.1.1 on 2020-10-23 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramaelectric', '0002_remove_contactpage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentform',
            name='date',
        ),
        migrations.AddField(
            model_name='appointmentform',
            name='day',
            field=models.CharField(default=True, max_length=50),
        ),
    ]
