# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-01 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0010_auto_20171101_1345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='idc',
            options={'verbose_name': 'IDC机房', 'verbose_name_plural': 'IDC机房'},
        ),
        migrations.AlterField(
            model_name='asset',
            name='tag',
            field=models.ManyToManyField(blank=True, default=1, to='asset.Tag'),
        ),
    ]
