# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 07:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_auto_20160621_1527'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-creation_date']},
        ),
    ]
