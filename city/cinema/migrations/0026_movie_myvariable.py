# Generated by Django 2.2.7 on 2019-12-13 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0025_auto_20191213_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='myVariable',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
