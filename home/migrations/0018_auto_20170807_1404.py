# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 18:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20170807_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 7, 14, 4, 10, 378495)),
        ),
    ]
