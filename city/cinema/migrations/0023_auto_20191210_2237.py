# Generated by Django 2.2.7 on 2019-12-10 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0022_auto_20191210_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
