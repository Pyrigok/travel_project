# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0003_auto_20180704_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record_for_travel_model',
            name='phone',
        ),
        migrations.AddField(
            model_name='record_for_travel_model',
            name='mail',
            field=models.CharField(verbose_name='Адреса електронної пошти', default=datetime.datetime(2018, 7, 4, 12, 2, 1, 313364, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
