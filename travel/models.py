# # -*- coding: utf-8 -*-
# from django.db import models
# from django.contrib.auth.models import User

# class UsProfile(models.Model):
# 	user = models.OneToOneField(User)

# 	class Meta(object):
# 		verbose_name = u'Профіль користувача'

# 	name = models.CharField(
# 		max_length = 30,
# 		blank = True,
# 		verbose_name = u"Ім'я користувача",
# 		default = '')

# 	def __str__(self):
# 		return self.user.username