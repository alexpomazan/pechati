# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-07-20 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pechati', '0003_auto_20190720_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='osnastka',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=4),
        ),
    ]