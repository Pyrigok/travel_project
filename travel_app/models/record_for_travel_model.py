# -*- coding: utf-8 -*-
from django.db import models

class Record_For_Travel_Model(models.Model):
	class Meta(object):
		verbose_name = u'Записані туристи'
		verbose_name_plural = u'Записані туристи'

	trip_name = models.ForeignKey('Trip_Description_Model',
		max_length = 25,
		blank = False,
		null = False,
		verbose_name = u'Пункт поїздки')

	first_name = models.CharField(
		max_length = 25,
		blank = False,
		null = False,
		verbose_name = u"Ім'я")

	last_name = models.CharField(
		max_length = 25,
		blank = False,
		null = False,
		verbose_name = u'Прізвище')

	mail = models.CharField(
		max_length = 50,
		blank = False,
		null = False,
		verbose_name = u'Адреса електронної пошти')

	date_of_join = models.DateField(
		auto_now_add = True,
		verbose_name = u'Дата заявки')

	def __str__(self):
		return u'%s, %s %s, %s, %s' %(self.trip_name, self.first_name, self.last_name, self.mail, self.date_of_join)