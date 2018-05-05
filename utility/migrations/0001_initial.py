# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-05 21:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_single', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=960)),
                ('location', models.CharField(max_length=240)),
                ('address', models.CharField(max_length=240)),
                ('city', models.CharField(max_length=240)),
                ('state', models.CharField(max_length=200)),
                ('zip_code', models.IntegerField(null=True)),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parentGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('minVolunteers', models.IntegerField()),
                ('maxVolunteers', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=240)),
                ('description', models.CharField(blank=True, max_length=960, null=True)),
                ('location', models.CharField(blank=True, max_length=240, null=True)),
                ('address', models.CharField(blank=True, max_length=240, null=True)),
                ('city', models.CharField(blank=True, max_length=240, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('paymentPerHour', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('parentEvent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utility.Event')),
            ],
        ),
        migrations.CreateModel(
            name='User_Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signin', models.DateTimeField(null=True)),
                ('signout', models.DateTimeField(null=True)),
                ('difference', models.CharField(max_length=100, null=True)),
                ('payment', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('parentSlot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utility.Slot')),
                ('volunteer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='slots',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slot_set', to='utility.Slot'),
        ),
    ]
