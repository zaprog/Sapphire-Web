# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-24 01:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='tagline',
            field=models.CharField(default=datetime.datetime(2018, 1, 24, 1, 15, 44, 496949, tzinfo=utc), max_length=120),
            preserve_default=False,
        ),
    ]