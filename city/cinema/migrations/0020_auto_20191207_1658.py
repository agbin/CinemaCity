# Generated by Django 2.2.7 on 2019-12-07 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0019_auto_20191207_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='genre',
            new_name='Genre',
        ),
    ]
