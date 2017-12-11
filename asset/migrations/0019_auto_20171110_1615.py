# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-10 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0018_auto_20171110_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device_status',
            old_name='name',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='server',
            name='device_status',
            field=models.IntegerField(choices=[(0, '在线'), (1, '已下线'), (2, '未知'), (3, '故障'), (4, '备用')], default=1, verbose_name='状态'),
        ),
    ]