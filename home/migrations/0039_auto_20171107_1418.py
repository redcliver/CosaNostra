# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 14:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_auto_20171107_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 7, 14, 18, 45, 404003)),
        ),
    ]