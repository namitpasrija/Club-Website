# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-13 08:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20171112_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventid', models.IntegerField()),
                ('mobile', models.CharField(max_length=20)),
                ('Fullname', models.CharField(max_length=100)),
                ('College', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=datetime.time(13, 58, 12, 948984)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.time(13, 58, 12, 948984)),
        ),
    ]