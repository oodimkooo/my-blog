# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-17 07:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0034_remove_blogpost_background_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='main_slide',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='on_slider',
        ),
    ]
