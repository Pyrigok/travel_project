# -*- coding: utf-8 -*-
from django.db import models

class Photo_Model(models.Model):
	class Meta(object):
		verbose_name = u'Фото'
		verbose_name_plural = u'Фото'

	photo_author = models.CharField(
		max_length = 50,
		blank = False,
		null = True,
		verbose_name = u'Автор фото')


	photo = models.ImageField(
		blank = False,
		verbose_name = u'Фото')

	travel_name_photo = models.ForeignKey('Travels_Model',
		max_length=50,
		blank = False,
		null = False,
		default = '',
		verbose_name = u'Подорож, до якої відноситься фото')

	photo_created_on = models.DateField(auto_now_add=True,
		verbose_name = u'Фото додане')

	def __str__ (self):
		return '%s, %s' %(self.photo_author, self.photo_created_on)