# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-08 20:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contato', 'verbose_name_plural': 'Contatos'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='kind',
            field=models.CharField(choices=[('E', 'E'), ('P', 'P')], max_length=1, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Speaker', verbose_name='Palestrante'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='value',
            field=models.CharField(max_length=255, verbose_name='Valor'),
        ),
    ]
