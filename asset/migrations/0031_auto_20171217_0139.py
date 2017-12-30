# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-16 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0030_auto_20171213_0021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='server',
            options={'permissions': (('delete_host', '删除主机'),), 'verbose_name': '服务器', 'verbose_name_plural': '服务器'},
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='cabinet_num',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='机柜位置'),
        ),
        migrations.AlterField(
            model_name='server',
            name='business_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.BusinessUnit', verbose_name='业务线'),
        ),
        migrations.AlterField(
            model_name='server',
            name='cabinet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.Cabinet', verbose_name='机柜位置'),
        ),
        migrations.AlterField(
            model_name='server',
            name='os_release',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='系统版本'),
        ),
        migrations.AlterField(
            model_name='server',
            name='os_type',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='系统平台'),
        ),
    ]
