# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-22 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote_machine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotesmain',
            name='title',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
