# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-26 05:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20170426_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 26, 5, 39, 34, 996449, tzinfo=utc), verbose_name='Дата начала'),
            preserve_default=False,
        ),
    ]