# Generated by Django 3.1.1 on 2020-10-28 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ramaelectric', '0029_auto_20201028_1249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='items',
            options={'ordering': ['-updated_on']},
        ),
    ]