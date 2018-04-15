#-*- coding: utf-8 -*-
"""
	DCAE - Publications - Admin:
		GenreAdmin, PublicationAdmin

	@author: mijomir mecu <self@mijomir.com>
"""
from django.contrib.admin.sites import site
from reversion import VersionAdmin

from .models import Genre, Publication


class GenreAdmin(VersionAdmin):
	list_display = ('id', 'name', 'timestamp',)
	list_display_links = ('id',)
	list_editable = ('name', )
	search_fields = ('name', 'description',)


class PublicationAdmin(VersionAdmin):
	list_display = ('id', 'gen', 'title', 'year', 'timestamp', 'public')
	list_display_links = ('id',)
	list_editable = ('public',)
	list_filter = ('gen', 'public',)
	search_fields = ('title', 'oauthors', 'publisher', 'city', 'review',
		'conference', 'other', 'abstract',)
	filter_horizontal = ('authors',)


site.register(Genre, GenreAdmin)
site.register(Publication, PublicationAdmin)
