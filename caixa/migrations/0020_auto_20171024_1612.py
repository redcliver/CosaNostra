# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-24 19:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0019_merge_20170815_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 24, 19, 12, 4, 754652, tzinfo=utc)),
        ),
    ]
