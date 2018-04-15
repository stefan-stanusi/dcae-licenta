#-*- coding: utf-8 -*-
"""
	DCAE - Announcements - Templatetags
	Registers a template tag, with cached output; retreives months/years when
	announcements have been posted
	Initialized in template

	@author: mijomir mecu <self@mijomir.com>
"""
import logging
from datetime import datetime

from django.core.cache import cache
from django import template

from announcements.models import Announcement

register = template.Library()
logger = logging.getLogger('app')


class GetAnnouncementArchivesNode(template.Node):

	def __init__(self, varname):
		self.varname = varname

	def render(self, context):
		key = 'dcae_archive'
		dt_archives = cache.get(key)

		if dt_archives is None:
			archives = {}

			# iterate over all published announcements
			for announcement in Announcement.objects.published().select_related():
				pub = announcement.date

				# see if we already have an announcement in this year
				if not archives.has_key(pub.year):
					 # if not, initialize a dict for the year
					archives[pub.year] = {}

				# make sure we know that we have an announcement posted in this month/year
				archives[pub.year][pub.month] = True

			dt_archives = []

			# now sort the years, so they don't appear randomly on the page
			years = list(int(k) for k in archives.keys())
			years.sort()
			# more recent years will appear first in the resulting collection
			years.reverse()

			 # iterate over all years
			for year in years:
				# sort the months of this year in which announcements were posted
				m = list(int(k) for k in archives[year].keys())
				m.sort()

				# now create a list of datetime objects for each month/year
				months = [datetime(year, month, 1) for month in m]

				# append this list to the final collection
				dt_archives.append( ( year, tuple(months) ) )

			cache.set(key, dt_archives)

		# put the collection into the context
		context[self.varname] = dt_archives
		return ''


def get_announcement_archives(parser, token):
	args = token.split_contents()
	argc = len(args)

	try:
		assert argc == 3 and args[1] == 'as'
	except AssertionError:
		raise template.TemplateSyntaxError('get_announcement_archives syntax: {% get_announcement_archives as varname %}')

	return GetAnnouncementArchivesNode(args[2])


register.tag(get_announcement_archives)
