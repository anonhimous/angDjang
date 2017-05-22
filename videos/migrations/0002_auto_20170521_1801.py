# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='embed',
            field=models.CharField(blank=True, help_text='YouTube embed code', max_length=120, null=True),
        ),
    ]
