# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
