#-*- coding: utf-8 -*-
"""
	DCAE - Menu - Templatetags
	Registers an inclusion tag, with cached output
	Initialized in urls.py

	@author: mijomir mecu <self@mijomir.com>
"""
import logging

from django.core.cache import cache
from django import template

from menu.models import MenuItem

register = template.Library()
logger = logging.getLogger('app')


def items():
	key = 'dcae_menu'
	items = cache.get(key)

	if not items:
		try:
			items = MenuItem.objects.all().prefetch_related('children').filter(m=1).filter(active=True)
			cache.set(key, items, 900) # setting the cache for 15 minutes
		except Exception, e:
			items = None
			logger.info(e)

	return {'items': items}

register.inclusion_tag('includes/menu.html')(items)
