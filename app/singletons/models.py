#-*- coding: utf-8 -*-
"""
	DCAE - Singletons - Models

	Models with a single instance

	@author: mijomir mecu <self@mijomir.com>
"""
from django.db.models import Model


class Singleton(Model):

	class Meta:
		abstract = True

	def save(self, *args, **kwargs):
		self.pk = 1
		super(Singleton, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		pass
