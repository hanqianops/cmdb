# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-01 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0008_auto_20171101_1040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpu',
            old_name='cpu_count',
            new_name='count',
        ),
        migrations.RenameField(
            model_name='cpu',
            old_name='cpu_model',
            new_name='speed',
        ),
        migrations.AddField(
            model_name='cpu',
            name='model',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='CPU型号'),
        ),
    ]
