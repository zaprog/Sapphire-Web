# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-21 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0027_slot_paymentperhour'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_slot',
            name='payment',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='paymentPerHour',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True),
        ),
    ]