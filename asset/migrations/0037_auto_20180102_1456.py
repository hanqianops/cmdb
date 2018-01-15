# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-02 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0036_userownedhost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userownedhost',
            name='host',
        ),
        migrations.RemoveField(
            model_name='userownedhost',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='host',
            field=models.ManyToManyField(to='asset.Server', verbose_name='主机'),
        ),
        migrations.DeleteModel(
            name='UserOwnedHost',
        ),
    ]