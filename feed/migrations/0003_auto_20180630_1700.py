# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-30 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_feed_entry_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed_entry',
            name='datetime',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='feed_entry',
            name='description',
            field=models.CharField(blank=True, max_length=960),
        ),
        migrations.AlterField(
            model_name='feed_entry',
            name='url',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
