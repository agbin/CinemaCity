# Generated by Django 2.2.7 on 2019-12-13 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0023_auto_20191210_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]