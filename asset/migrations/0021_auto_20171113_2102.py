# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-13 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0020_auto_20171113_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='name',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='主机名'),
        ),
    ]
