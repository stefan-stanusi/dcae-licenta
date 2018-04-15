#-*- coding: utf-8 -*-
"""
	DCAE - Menu - Models:
		Menu, MenuItem

	Defines a singleton model allowing admins to control the site-wide menu
	Menu Items should be a set of inlines
	The output should be stored in a template tag which will be loaded when the
	request is initialized (namely in urls.py)
	The output should be stored in memcache; cache invalidated on save

	@author: mijomir mecu <self@mijomir.com>
"""
import logging
from datetime import datetime

from django.core.cache import cache
from django.db.models import Model, CharField, URLField, DateTimeField, \
	ForeignKey, BooleanField, SmallIntegerField
from django.utils.translation import ugettext_lazy as _

from singletons.models import Singleton
from datatrans.utils import register

logger = logging.getLogger('apps')


class Menu(Singleton):
	edited = DateTimeField(auto_now=True, db_index=True)

	class Meta:
		verbose_name = u'Menu'
		verbose_name_plural = u'Menu'
		ordering = ('id',)

	def __unicode__(self):
		return u'Menu'

	# overriding the save method to invalidate the cache;
	# singleton save method added
	def save(self, *args, **kwargs):
		self.pk = 1
		super(Menu, self).save(*args, **kwargs)
		# post save
		key = 'dcae_menu'
		try:
			cache.delete(key)
		except Exception, e:
			# catch and log any exception
			logger.info(e)


class MenuItem(Model):
	m = ForeignKey(Menu)
	name = CharField(max_length=100, db_index=True, verbose_name=_(u'Displayed \
		name'), help_text=_(u'Required field, max 100 characters. This is the \
		text to be shown in the menu.'))
	url = URLField(max_length=255, verbose_name=_(u'URL'),
		help_text=_(u'Optional field, max 255 characters. The target for the \
		menu item anchor.'), blank=True)
	parent = ForeignKey('self', blank=True, null=True, related_name='children',
		help_text=_(u'If this item should be displayed in the dropdown, please \
		select its parent; optional filed.'))
	nofollow = BooleanField(default=False, help_text=_(u'Check to add a nofollow\
	 value to the attribute "rel"; this attribute instructs web spiders to \
	ignore the target of the link; it is usually used for external pages.'))
	blank = BooleanField(default=False, verbose_name=_(u'Open in a new tab'),
		help_text=_(u'Check if you want the target page to be opened in a new\
		tab/window.'))
	o = SmallIntegerField(blank=True, null=True, verbose_name=_(u'Order'),
		help_text=_(u'Optional field, only numeric values allowed. Defines the \
		order of the item in the menu.'))
	active = BooleanField(default=True, db_index=True, help_text=_(u'Uncheck \
		if you want the item to disappear from the menu; ir can be reactivated\
		 at any time by checking this checbox.'))

	class Meta:
		verbose_name =u'Menu Item'
		verbose_name_plural = u'Menu Items'
		ordering = ('o', 'id',)

	def __unicode__(self):
		return u'%s' % self.name


class MenuItemTranslation(object):
	fields = ('name',)

register(MenuItem, MenuItemTranslation)
