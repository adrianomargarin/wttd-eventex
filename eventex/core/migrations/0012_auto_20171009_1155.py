# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-09 11:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20171009_0320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talk',
            options={'ordering': ['start'], 'verbose_name': 'Palestra', 'verbose_name_plural': 'Palestras'},
        ),
    ]
