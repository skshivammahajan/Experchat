# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experchat', '0011_auto_20170512_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertprofile',
            name='review_status',
            field=models.PositiveSmallIntegerField(choices=[(3, 'APPROVED_BY_SUPER_ADMIN'), (1, 'NOT_SUBMITTED_FOR_REVIEW'), (4, 'REJECTED_BY_SUPER_ADMIN'), (2, 'SUBMITTED_FOR_REVIEW')], default=1, verbose_name='profile review status'),
        ),
    ]
