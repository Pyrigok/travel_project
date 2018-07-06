# -*- coding: utf-8 -*-
from django.db import models

class Respond_Model(models.Model):
	class Meta(object):
		verbose_name = u'Відгуки'
		verbose_name_plural = u'Відгуки'

	respond_author = models.CharField(
		max_length = 50,
		blank = False,
		null = False,
		verbose_name = u'Автор відгука')

	respond_text = models.TextField(
		blank = False,
		null = False,
		verbose_name = u'Відгук')

	respond_created_on = models.DateField(
		auto_now_add=True,
		verbose_name = u'Запис створений - ')

	def __str__(self):
		return '%s - %s, %s' %(self.respond_author, self.respond_text, self.respond_created_on)