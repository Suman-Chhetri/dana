# Generated by Django 2.1.4 on 2019-03-29 07:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20190329_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='dateAdded',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 29, 7, 20, 34, 681885, tzinfo=utc)),
        ),
    ]
