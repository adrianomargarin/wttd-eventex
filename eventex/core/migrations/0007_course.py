# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-09 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20171008_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('start', models.TimeField(blank=True, null=True, verbose_name='Início')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('slots', models.IntegerField()),
                ('speakers', models.ManyToManyField(blank=True, to='core.Speaker', verbose_name='Palestrantes')),
            ],
            options={
                'verbose_name': 'Palestra',
                'abstract': False,
                'verbose_name_plural': 'Palestras',
            },
        ),
    ]