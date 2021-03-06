# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 07:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='raid_type',
        ),
        migrations.RemoveField(
            model_name='server',
            name='server_attr',
        ),
        migrations.AddField(
            model_name='server',
            name='sub_asset_type',
            field=models.SmallIntegerField(choices=[(0, '物理服务器'), (1, '宿主机'), (2, '虚拟机')], default=0, verbose_name='服务器类型'),
        ),
        migrations.AlterField(
            model_name='server',
            name='upper_layer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='upperlayer', to='asset.Server', verbose_name='关联设备'),
        ),
    ]
