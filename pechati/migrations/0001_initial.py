# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-07-19 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pechat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
