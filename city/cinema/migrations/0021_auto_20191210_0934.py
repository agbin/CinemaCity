# Generated by Django 2.2.7 on 2019-12-10 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0020_auto_20191207_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='last_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='last_date'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='start_date'),
        ),
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together=set(),
        ),
    ]
