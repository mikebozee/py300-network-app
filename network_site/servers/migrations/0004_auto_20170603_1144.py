# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 18:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0003_router_notes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='router',
            options={'ordering': ['order']},
        ),
    ]
