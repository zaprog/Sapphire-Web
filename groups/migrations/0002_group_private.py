# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-05 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]