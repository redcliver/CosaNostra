# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 19:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_auto_20171031_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 31, 19, 46, 5, 492558)),
        ),
    ]
