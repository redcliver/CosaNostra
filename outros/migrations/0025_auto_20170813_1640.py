# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 20:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outros', '0024_auto_20170808_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 13, 16, 40, 4, 963490)),
        ),
        migrations.AlterField(
            model_name='comanda_corte',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 13, 16, 40, 4, 967492)),
        ),
    ]