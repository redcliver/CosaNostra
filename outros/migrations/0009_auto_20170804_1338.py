# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 17:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outros', '0008_auto_20170801_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 4, 13, 38, 53, 721520)),
        ),
    ]