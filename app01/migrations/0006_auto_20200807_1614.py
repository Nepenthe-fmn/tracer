# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-08-07 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20200807_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='项目名称'),
        ),
    ]
