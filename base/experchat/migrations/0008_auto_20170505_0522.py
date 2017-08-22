# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 05:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experchat', '0007_auto_20170427_0639'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertNotificationSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='created timestamp')),
                ('modified_timestamp', models.DateTimeField(auto_now=True, verbose_name='modified timestamp')),
                ('code', models.CharField(choices=[('daily-summary-report', 'DAILY_SUMMARY_REPORT'), ('review-session', 'REVIEW_SESSION')], max_length=32, verbose_name='code')),
                ('status', models.BooleanField(default=True, verbose_name='code status')),
                ('userbase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_settings', to=settings.AUTH_USER_MODEL, verbose_name='userbase')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='expertnotificationsettings',
            unique_together=set([('userbase', 'code')]),
        ),
    ]
