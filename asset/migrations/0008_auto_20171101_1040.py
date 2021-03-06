# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-01 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0007_auto_20171031_1927'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cpu',
            options={'verbose_name': 'CPU', 'verbose_name_plural': 'CPU'},
        ),
        migrations.AlterModelOptions(
            name='mem',
            options={'verbose_name': '内存', 'verbose_name_plural': '内存'},
        ),
        migrations.RemoveField(
            model_name='cpu',
            name='cpu_physical_count',
        ),
        migrations.AlterField(
            model_name='cpu',
            name='cpu_count',
            field=models.IntegerField(verbose_name='CPU核心'),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='cpu_model',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='CPU主频'),
        ),
    ]
