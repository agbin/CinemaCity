# Generated by Django 2.2.7 on 2019-12-14 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0027_auto_20191213_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='end',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='start',
            field=models.DateField(null=True),
        ),
    ]
