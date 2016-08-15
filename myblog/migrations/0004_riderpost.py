# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20160614_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiderPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='ФИО')),
                ('shortinfo', models.TextField(blank=True, max_length=5000, null=True, verbose_name='О себе')),
            ],
        ),
    ]
