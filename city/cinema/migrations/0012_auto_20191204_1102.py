# Generated by Django 2.2.7 on 2019-12-04 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0011_auto_20191203_1717'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together={('id', 'Title')},
        ),
        migrations.RemoveField(
            model_name='movie',
            name='title',
        ),
    ]