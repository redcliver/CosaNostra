# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 16:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outros', '0034_auto_20171026_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='qnt',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 30, 13, 38, 55, 293157)),
        ),
        migrations.AlterField(
            model_name='comanda_corte',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 30, 13, 38, 55, 293157)),
        ),
    ]