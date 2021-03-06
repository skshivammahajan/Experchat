# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 18:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='created timestamp')),
                ('modified_timestamp', models.DateTimeField(auto_now=True, verbose_name='modified timestamp')),
                ('last_4', models.CharField(max_length=4, verbose_name='last 4 digits of card')),
                ('is_default', models.BooleanField(default=False, verbose_name='is default')),
                ('payment_method_token', models.CharField(max_length=50, verbose_name='payment method token')),
                ('expiration_date', models.CharField(max_length=7, verbose_name='expiration date')),
                ('card_type', models.CharField(max_length=50, verbose_name='card type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='created timestamp')),
                ('modified_timestamp', models.DateTimeField(auto_now=True, verbose_name='modified timestamp')),
                ('customer_uid', models.CharField(max_length=50, verbose_name='customer uid')),
                ('gateway', models.IntegerField(default=1, verbose_name='gateway')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='created timestamp')),
                ('modified_timestamp', models.DateTimeField(auto_now=True, verbose_name='modified timestamp')),
                ('transaction_uid', models.CharField(max_length=50, verbose_name='transaction uid')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Unsettled Transaction'), (2, 'Settled Transaction'), (3, 'Cancelled Transaction'), (4, 'Failed Transaction')], default=1, verbose_name='status')),
                ('amount', models.CharField(max_length=50, verbose_name='amount')),
                ('card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to='payments.Card', verbose_name='user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='card',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='payments.Customer', verbose_name='customer'),
        ),
    ]
