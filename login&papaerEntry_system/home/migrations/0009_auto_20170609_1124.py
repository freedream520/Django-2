# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20170609_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.TextField(default='123'),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.TextField(default='123'),
        ),
        migrations.AddField(
            model_name='user',
            name='jobTitle',
            field=models.TextField(default='123'),
        ),
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.TextField(default='123'),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.TextField(default='123'),
        ),
    ]
