# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-07-20 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pechati', '0002_osnastka'),
    ]

    operations = [
        migrations.AddField(
            model_name='osnastka',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images/'),
        ),
        migrations.AddField(
            model_name='pechat',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images/'),
        ),
    ]
