# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-21 07:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbsettings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Settings',
            new_name='Root',
        ),
    ]
