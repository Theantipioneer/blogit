# Generated by Django 3.1.4 on 2020-12-23 03:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_auto_20201222_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 3, 25, 49, 525068, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 3, 25, 49, 525068, tzinfo=utc)),
        ),
    ]
