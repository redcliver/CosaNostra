# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 15:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outros', '0026_auto_20170814_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 14, 11, 51, 22, 568161)),
        ),
        migrations.AlterField(
            model_name='comanda_corte',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 14, 11, 51, 22, 580169)),
        ),
    ]
