# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-13 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0022_mytask_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytask',
            name='is_complited',
            field=models.BooleanField(default=True, verbose_name='Выполнено?'),
        ),
    ]
