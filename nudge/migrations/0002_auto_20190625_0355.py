# Generated by Django 2.2.2 on 2019-06-25 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nudge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubevents',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]
