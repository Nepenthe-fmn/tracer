# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-08-09 13:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0012_auto_20200809_1739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectuser',
            old_name='start',
            new_name='star',
        ),
    ]
