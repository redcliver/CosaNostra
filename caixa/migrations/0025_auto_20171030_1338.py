# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 16:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0024_auto_20171026_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 30, 16, 38, 55, 293157, tzinfo=utc)),
        ),
    ]
