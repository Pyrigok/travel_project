# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record_for_travel_model',
            name='last_name',
            field=models.CharField(verbose_name='Прізвище', max_length=25),
        ),
    ]
