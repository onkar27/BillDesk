# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-27 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_prod_val_gst_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prod_val',
            name='gst_in',
            field=models.CharField(blank=True, default=None, max_length=15),
        ),
    ]
