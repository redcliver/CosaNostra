# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20170808_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
