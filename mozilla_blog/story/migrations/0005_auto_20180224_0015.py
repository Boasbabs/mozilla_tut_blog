# Generated by Django 2.0.2 on 2018-02-24 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_auto_20180223_2333'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]