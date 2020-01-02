# Generated by Django 2.2.7 on 2019-12-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0010_auto_20191203_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='title',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together={('id', 'title')},
        ),
    ]
