# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-07-21 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pechati', '0005_klishe'),
    ]

    operations = [
        migrations.AddField(
            model_name='pechat',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
