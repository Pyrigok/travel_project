# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_author', models.CharField(max_length=50, null=True, verbose_name='Автор фото')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото')),
                ('photo_created_on', models.DateField(verbose_name='Фото додане', auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Фото',
                'verbose_name': 'Фото',
            },
        ),
        migrations.CreateModel(
            name='Record_For_Travel_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name="Ім'я")),
                ('last_name', models.DateField(max_length=25, verbose_name='Прізвище')),
                ('phone', models.IntegerField(verbose_name='Номер телефону')),
                ('date_of_join', models.DateField(verbose_name='Дата заявки', auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Записані туристи',
                'verbose_name': 'Записані туристи',
            },
        ),
        migrations.CreateModel(
            name='Respond_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respond_author', models.CharField(max_length=50, verbose_name='Автор відгука')),
                ('respond_text', models.TextField(verbose_name='Відгук')),
                ('respond_created_on', models.DateField(verbose_name='Запис створений - ', auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Відгуки',
                'verbose_name': 'Відгуки',
            },
        ),
        migrations.CreateModel(
            name='Travels_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_photo', models.ImageField(upload_to='', verbose_name='Фото автора')),
                ('travel_author', models.CharField(max_length=50, verbose_name='Автор')),
                ('travel_name', models.CharField(max_length=50, verbose_name='Назва подорожі')),
                ('travel_route', models.CharField(max_length=500, blank=True, null=True, verbose_name='Довжина і час проходження')),
                ('travel_description', models.CharField(max_length=500, verbose_name='Опис подорожі')),
                ('travel_cover', models.ImageField(upload_to='', default='', verbose_name='Обкладинка альбому')),
                ('travel_created_on', models.DateField(verbose_name='Подорож додана', auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Альбоми',
                'verbose_name': 'Альбоми',
            },
        ),
        migrations.CreateModel(
            name='Trip_Description_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_organizer', models.CharField(max_length=50, verbose_name='Організатор поїздки')),
                ('trip_point', models.CharField(max_length=25, verbose_name='Пункт поїздки')),
                ('trip_description', models.CharField(max_length=100, verbose_name='Опис маршруту')),
                ('number_of_seats', models.IntegerField(verbose_name='Кількість можливих місць')),
                ('departure_date', models.DateField(verbose_name='Дата виїзду')),
                ('date_of_arrival', models.DateField(verbose_name='Дата приїзду')),
                ('trip_created_on', models.DateField(verbose_name='Запис створено', auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Плановані подорожі',
                'verbose_name': 'Плановані подорожі',
            },
        ),
        migrations.AddField(
            model_name='record_for_travel_model',
            name='trip_name',
            field=models.ForeignKey(max_length=25, to='travel_app.Trip_Description_Model', verbose_name='Пункт поїздки'),
        ),
        migrations.AddField(
            model_name='photo_model',
            name='travel_name_photo',
            field=models.ForeignKey(max_length=50, to='travel_app.Travels_Model', verbose_name='Подорож, до якої відноситься фото', default=''),
        ),
    ]
