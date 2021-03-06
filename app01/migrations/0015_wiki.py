# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-08-11 12:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0014_auto_20200811_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('deepth', models.IntegerField(default=1, verbose_name='深度')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='app01.Wiki', verbose_name='父文章')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Project', verbose_name='项目')),
            ],
        ),
    ]
