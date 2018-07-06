# -*- coding: utf-8 -*-
from django.db import models

class Trip_Description_Model(models.Model):
	class Meta(object):
		verbose_name = u'Плановані подорожі'
		verbose_name_plural = u'Плановані подорожі'

	trip_organizer = models.CharField(
		max_length = 50,
		blank = False,
		null = False,
		verbose_name = u'Організатор поїздки')

	trip_point = models.CharField(
		max_length = 25,
		blank = False,
		null = False,
		verbose_name = u'Пункт поїздки')

	trip_description = models.CharField(
		max_length = 100,
		blank = False,
		null = False,
		verbose_name = u'Опис маршруту')

	number_of_seats = models.IntegerField(
		blank = False,
		null = False,
		verbose_name = u'Кількість можливих місць')

	departure_date = models.DateField(
		blank = False,
		verbose_name = u'Дата виїзду')

	date_of_arrival = models.DateField(
		blank = False,
		verbose_name = u'Дата приїзду')

	trip_created_on = models.DateField(
		auto_now_add = True,
		verbose_name = u'Запис створено')

	def __str__(self):
		return u'%s' %(self.trip_point)