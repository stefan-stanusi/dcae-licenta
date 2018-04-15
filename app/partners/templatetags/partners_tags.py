#-*- coding: utf-8 -*-
"""
	DCAE - Partners - Templatetags
	Registers an inclusion tag, with cached output
	Initialized in template

	@author: mijomir mecu <self@mijomir.com>
"""
import logging

from django.core.cache import cache
from django import template

from partners.models import Partner

register = template.Library()
logger = logging.getLogger('apps')


def get_partners():
	key = 'dcae_partners'
	partners = cache.get(key)

	if not partners:
		try:
			partners = Partner.objects.all().filter(public=True)
			cache.set(key, partners, 900)
		except Exception, e:
			partners = None
			logger.info(e)

	return {'partners': partners}

register.inclusion_tag('includes/partners.html')(get_partners)
