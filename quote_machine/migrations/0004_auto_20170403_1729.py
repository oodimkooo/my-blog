# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-03 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote_machine', '0003_remove_quotesmain_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotesmain',
            name='publisher',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Запостил'),
        ),
    ]
