# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-15 05:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0026_mytask_is_deleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mytask',
            old_name='is_complited',
            new_name='is_completed',
        ),
    ]
