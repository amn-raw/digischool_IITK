# Generated by Django 4.0.1 on 2022-03-24 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='available_courses',
            name='forum_series_number',
            field=models.IntegerField(default=0),
        ),
    ]
