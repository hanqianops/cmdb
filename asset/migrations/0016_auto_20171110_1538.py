# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-10 07:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0015_auto_20171110_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='server',
            old_name='device_status_id',
            new_name='device_status',
        ),
    ]
