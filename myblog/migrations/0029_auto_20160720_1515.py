# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-20 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0028_auto_20160720_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='_fulltext_rendered',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='_shortcontent_rendered',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='fulltext',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Полный текст'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='shortcontent',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Краткое содержание'),
        ),
    ]
