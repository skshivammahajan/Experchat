# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experchat', '0002_expert_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyexpertstats',
            name='revenue',
            field=models.FloatField(default=0),
        ),
    ]
