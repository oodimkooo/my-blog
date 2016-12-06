# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-06 04:54
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0043_auto_20161108_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='shortcontent',
            field=tinymce.models.HTMLField(blank=True, max_length=1000, null=True, verbose_name='Краткое содержание'),
        ),
    ]
