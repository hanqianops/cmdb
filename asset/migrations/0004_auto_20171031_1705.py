# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 09:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20171031_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='networkdevice',
            old_name='sub_asset_type',
            new_name='network_device_type',
        ),
    ]
