# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.URLField(blank=True, max_length=384, null=True, verbose_name='Feed Image URL'),
        ),
    ]
