# Generated by Django 3.1.1 on 2020-10-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramaelectric', '0024_auto_20201028_1145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='items',
            options={'get_latest_by': ['-updated_on']},
        ),
        migrations.AlterField(
            model_name='items',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
