# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-01-28 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotationweb', '0020_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='shuffle_videos',
            field=models.BooleanField(default=True, help_text='Shuffle videos'),
        ),
    ]
