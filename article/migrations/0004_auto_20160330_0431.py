# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-03-30 04:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20160330_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='data_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 30, 4, 31, 14, 738935, tzinfo=utc)),
        ),
    ]