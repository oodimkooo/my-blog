# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-07 00:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0046_auto_20161206_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mytask',
            name='author',
        ),
        migrations.DeleteModel(
            name='RiderPost',
        ),
        migrations.RemoveField(
            model_name='sliderpost',
            name='image_link',
        ),
        migrations.RemoveField(
            model_name='sliderpost',
            name='main_post',
        ),
        migrations.DeleteModel(
            name='MyTask',
        ),
        migrations.DeleteModel(
            name='SliderPost',
        ),
    ]