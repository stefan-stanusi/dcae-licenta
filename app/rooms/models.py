#-*- coding: utf-8 -*-
"""
	DCAE - Rooms - Models:
		Room

	@author: mijomir mecu <self@mijomir.com>
"""
from datetime import datetime

from django.db.models import Model, CharField, SlugField, TextField, \
	DateTimeField, BooleanField
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from datatrans.utils import register


class Room(Model):
	name = CharField(max_length=255, db_index=True, verbose_name=_(u'Name'),
		help_text=_(u'Required field, max 255 characters. Eg. Sala 405'))
	slug = SlugField(db_index=True, max_length=255, help_text=_(u'Required \
		field. It autocompletes as you write the name. Edit only if necessary.'))
	description = TextField(blank=True, verbose_name=_(u'Directions'),
		help_text=_(u'Optional field'))
	program = TextField(blank=True, verbose_name=_(u'Room\'s program'),
		help_text=_(u'Optional field'))
	timestamp = DateTimeField(auto_now=True, db_index=True)
	public = BooleanField(default=False, help_text=_(u'Check to make the \
		room visible on the website'))

	class Meta:
		verbose_name = _(u'Room')
		verbose_name_plural = _(u'Rooms')
		ordering = ('name', 'id',)

	def __unicode__(self):
		return u'%s' % self.name

	def save(self, *args, **kwargs):
		# before save, make sure there is a slug
		if not self.slug:
			self.slug = slugify(self.name)

		# send data to the database
		super(Room, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return '/sali/%s/%s/' % (self.id, self.slug)


class RoomTranslation(object):
	fields = ('name', 'description', 'program',)


register(Room, RoomTranslation)
