# Generated by Django 4.0.3 on 2022-08-19 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0006_available_courses_news_series_number_all_anouncement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_anouncement',
            name='news_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='all_anouncement',
            name='news_title',
            field=models.TextField(),
        ),
    ]
