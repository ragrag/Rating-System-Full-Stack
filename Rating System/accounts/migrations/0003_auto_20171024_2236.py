# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-24 20:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_username2'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group',
            new_name='Team',
        ),
    ]