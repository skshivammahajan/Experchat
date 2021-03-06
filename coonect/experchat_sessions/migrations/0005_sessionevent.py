# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-01 10:13
from __future__ import unicode_literals

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('experchat_sessions', '0004_auto_20170501_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='created timestamp')),
                ('modified_timestamp', models.DateTimeField(auto_now=True, verbose_name='modified timestamp')),
                ('session_id', models.CharField(max_length=100, verbose_name='Session ID')),
                ('event', models.CharField(max_length=50, verbose_name='Event')),
                ('event_date_time', models.DateTimeField(verbose_name='Event Date Time')),
                ('connection_id', models.CharField(max_length=100, verbose_name='Connection ID')),
                ('event_reason', models.CharField(blank=True, max_length=200, null=True, verbose_name='Reason')),
                ('event_data', django_mysql.models.JSONField(default=dict, verbose_name='Event Data')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
