# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-15 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0025_auto_20160714_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytask',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Отменено?'),
        ),
    ]
