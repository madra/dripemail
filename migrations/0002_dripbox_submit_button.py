# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dripemail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dripbox',
            name='submit_button',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Submit Button text'),
        ),
    ]
