# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-08 16:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]
