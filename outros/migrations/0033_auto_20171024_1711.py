# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-24 20:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outros', '0032_auto_20171024_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 24, 17, 11, 54, 788309)),
        ),
        migrations.AlterField(
            model_name='comanda_corte',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 24, 17, 11, 54, 792812)),
        ),
    ]
