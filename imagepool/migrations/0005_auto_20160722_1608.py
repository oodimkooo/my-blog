# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-22 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagepool', '0004_auto_20160721_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepool',
            name='image',
            field=models.ImageField(default=None, upload_to='%Y/%m', verbose_name='Изображение'),
        ),
    ]
