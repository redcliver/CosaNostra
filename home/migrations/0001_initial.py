# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 14:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comanda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateTimeField(default=datetime.datetime(2017, 8, 1, 10, 8, 48, 546224))),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qnt', models.IntegerField()),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='produto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='servico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='produto1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.produto'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='produtos',
            field=models.ManyToManyField(to='home.item'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='servicos',
            field=models.ManyToManyField(to='home.servico'),
        ),
    ]
