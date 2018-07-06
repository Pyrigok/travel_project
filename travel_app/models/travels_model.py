# -*- coding: utf-8 -*-
from django.db import models

class Travels_Model(models.Model):
	class Meta(object):
		verbose_name = 'Альбоми'
		verbose_name_plural = 'Альбоми'


	author_photo = models.ImageField(
		blank = False,
		verbose_name = u'Фото автора')

	travel_author = models.CharField(
		max_length = 50,
		blank = False,
		null = False,
		verbose_name = u'Автор')

	travel_name = models.CharField(
		max_length = 50,
		blank = False,
		null = False,
		verbose_name = u'Назва подорожі')

	travel_route = models.CharField(
		max_length = 500,
		blank = True,
		null = True,
		verbose_name = u'Довжина і час проходження')

	travel_description = models.CharField(
		max_length = 500,
		blank = False,
		null = False,
		verbose_name = u'Опис подорожі')

	travel_cover = models.ImageField(
		blank = False,
		default = '',
		verbose_name = u'Обкладинка альбому')

	travel_created_on = models.DateField(auto_now_add=True,
		verbose_name = u'Подорож додана')


	def __str__(self):
		return '%s' %(self.travel_name)