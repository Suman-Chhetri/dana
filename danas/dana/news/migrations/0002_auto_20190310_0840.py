# Generated by Django 2.1.4 on 2019-03-10 08:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='dateAdded',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 10, 8, 40, 41, 59559, tzinfo=utc)),
        ),
    ]