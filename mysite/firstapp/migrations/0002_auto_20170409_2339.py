# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 02:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tesxt',
            new_name='text',
        ),
    ]
