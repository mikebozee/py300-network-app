# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0006_auto_20170603_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
