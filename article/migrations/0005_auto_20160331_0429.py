# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-03-31 04:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20160330_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='article',
            name='data_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 31, 4, 29, 36, 336527, tzinfo=utc)),
        ),
    ]