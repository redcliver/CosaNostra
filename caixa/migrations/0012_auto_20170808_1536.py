# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 19:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0011_auto_20170807_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 8, 15, 36, 47, 929493)),
        ),
    ]