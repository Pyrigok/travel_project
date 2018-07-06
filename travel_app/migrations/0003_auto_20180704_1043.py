# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0002_auto_20180704_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record_for_travel_model',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Номер телефону'),
        ),
    ]
