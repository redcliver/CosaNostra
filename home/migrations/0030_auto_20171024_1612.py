# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-24 19:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_merge_20170815_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 24, 16, 12, 4, 758154)),
        ),
    ]
