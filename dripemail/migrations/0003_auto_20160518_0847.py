# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 08:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dripemail', '0002_dripbox_submit_button'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='user email.', max_length=254)),
                ('name', models.CharField(max_length=1000, verbose_name='Lead Name')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('dripbox', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead_capture_box', to='dripemail.Dripbox')),
            ],
        ),
        migrations.RemoveField(
            model_name='webrequest',
            name='cookies',
        ),
        migrations.RemoveField(
            model_name='webrequest',
            name='get',
        ),
        migrations.RemoveField(
            model_name='webrequest',
            name='is_ajax',
        ),
        migrations.RemoveField(
            model_name='webrequest',
            name='is_secure',
        ),
        migrations.RemoveField(
            model_name='webrequest',
            name='post',
        ),
        migrations.RemoveField(
            model_name='webrequest',
            name='raw_post',
        ),
        migrations.RemoveField(
            model_name='webrequest',
            name='status_code',
        ),
        migrations.RemoveField(
            model_name='webrequest',
            name='user',
        ),
        migrations.AddField(
            model_name='lead',
            name='request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dripemail.WebRequest'),
        ),
    ]
