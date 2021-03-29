# Generated by Django 3.1.7 on 2021-03-29 02:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='keyword_occurrence',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='musician',
            name='keywords',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='musician',
            name='list_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 29, 8, 43, 56, 275563)),
        ),
    ]
