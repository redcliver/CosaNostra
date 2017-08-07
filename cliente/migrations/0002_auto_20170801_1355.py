# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='telefone',
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefone2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
