# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 19:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outros', '0020_auto_20170807_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 7, 15, 59, 21, 416082)),
        ),
        migrations.AlterField(
            model_name='comanda_corte',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 7, 15, 59, 21, 420084)),
        ),
    ]