# Generated by Django 2.0.2 on 2018-02-23 23:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_auto_20180223_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date posted'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='post_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='time posted'),
        ),
    ]
