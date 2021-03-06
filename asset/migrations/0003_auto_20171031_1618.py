# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 08:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_auto_20171031_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='business_unit',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='device_type',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='idc',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='eventlog',
            name='asset',
        ),
        migrations.RemoveField(
            model_name='networkdevice',
            name='asset',
        ),
        migrations.RemoveField(
            model_name='server',
            name='asset',
        ),
        migrations.AddField(
            model_name='idc',
            name='address',
            field=models.CharField(blank=True, max_length=100, verbose_name='机房地址'),
        ),
        migrations.AddField(
            model_name='idc',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='到期日期'),
        ),
        migrations.AddField(
            model_name='idc',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='租赁日期'),
        ),
        migrations.AddField(
            model_name='server',
            name='business_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.BusinessUnit', verbose_name='所属业务线'),
        ),
        migrations.AddField(
            model_name='server',
            name='device_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.Manufactory', verbose_name='设备厂商'),
        ),
        migrations.AddField(
            model_name='server',
            name='expire_date',
            field=models.DateField(blank=True, null=True, verbose_name='过保修期'),
        ),
        migrations.AddField(
            model_name='server',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.IDC', verbose_name='IDC机房'),
        ),
        migrations.AddField(
            model_name='server',
            name='server_attr',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='设备型号'),
        ),
        migrations.AddField(
            model_name='server',
            name='sn',
            field=models.CharField(default='ddd', max_length=128, unique=True, verbose_name='资产SN号'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='server',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '在线'), (1, '已下线'), (2, '未知'), (3, '故障'), (4, '备用')], default=0, verbose_name='资产状态'),
        ),
        migrations.AddField(
            model_name='server',
            name='tags',
            field=models.ManyToManyField(blank=True, default=1, to='asset.Tag'),
        ),
        migrations.AddField(
            model_name='server',
            name='trade_date',
            field=models.DateField(blank=True, null=True, verbose_name='购买时间'),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Server', verbose_name='所属服务器'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Server', verbose_name='所属服务器'),
        ),
        migrations.AlterField(
            model_name='mem',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Server', verbose_name='所属服务器'),
        ),
        migrations.AlterField(
            model_name='nic',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Server', verbose_name='所属服务器'),
        ),
        migrations.AlterUniqueTogether(
            name='disk',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='nic',
            unique_together=set([]),
        ),
        migrations.DeleteModel(
            name='Asset',
        ),
    ]
