# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-23 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagepool', '0012_auto_20160816_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagepool',
            name='is_commentable',
            field=models.BooleanField(default=True, verbose_name='Комментарии'),
        ),
    ]
