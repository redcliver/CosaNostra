# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 17:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20170805_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 7, 13, 57, 31, 859014)),
        ),
    ]