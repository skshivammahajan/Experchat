# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experchat', '0004_auto_20170414_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecsession',
            name='card',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='card'),
        ),
    ]
