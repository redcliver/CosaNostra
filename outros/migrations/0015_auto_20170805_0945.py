# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 13:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outros', '0014_auto_20170805_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 5, 9, 45, 38, 151382)),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='telefone1',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
