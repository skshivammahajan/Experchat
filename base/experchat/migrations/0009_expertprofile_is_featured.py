# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-08 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experchat', '0008_auto_20170505_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertprofile',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='Is featured Expert'),
        ),
    ]
