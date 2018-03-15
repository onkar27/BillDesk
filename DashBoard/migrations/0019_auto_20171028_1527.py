# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-28 09:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0018_auto_20171028_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='onk_rBill_Inven',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='onk_rBilling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saletime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('tot_price', models.IntegerField(default=0)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='onk_rCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=b'ID')),
                ('c_name', models.CharField(max_length=100)),
                ('age_group', models.IntegerField()),
                ('village', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('gst_in', models.CharField(default=b'', max_length=15)),
                ('del_flag', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['c_name'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='onk_rInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=b'ID')),
                ('i_name', models.CharField(max_length=100)),
                ('i_price', models.IntegerField(default=0)),
                ('gst_perc', models.IntegerField(default=0)),
                ('del_flag', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['i_name'],
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='onk_rbilling',
            name='Customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customer_id', to='DashBoard.onk_rCustomer'),
        ),
        migrations.AddField(
            model_name='onk_rbill_inven',
            name='Billing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashBoard.onk_rBilling'),
        ),
        migrations.AddField(
            model_name='onk_rbill_inven',
            name='Inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashBoard.onk_rInventory'),
        ),
    ]