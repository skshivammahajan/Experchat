# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-15 11:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tagstats',
            options={'ordering': ('-last_week_search_count',)},
        ),
    ]
