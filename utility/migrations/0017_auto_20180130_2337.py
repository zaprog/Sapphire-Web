# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-31 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0016_auto_20180130_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_slot',
            name='signin',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='user_slot',
            name='signout',
            field=models.DateTimeField(null=True),
        ),
    ]