# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0008_router_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='router',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
