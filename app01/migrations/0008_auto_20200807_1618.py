# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-08-07 08:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_auto_20200807_1615'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('name', 'create')]),
        ),
    ]
