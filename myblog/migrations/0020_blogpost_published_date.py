# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-13 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0019_blogpost_is_commentable'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации'),
        ),
    ]
