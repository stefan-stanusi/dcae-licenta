#-*- coding: utf-8 -*-
"""
	DCAE - Master - Admin:
		ProgrammeAdmin

	@author: mijomir mecu <self@mijomir.com>
"""
from django.contrib.admin.sites import site
from reversion import VersionAdmin

from .models import Programme


class ProgrammeAdmin(VersionAdmin):
	class Media:
		js = (
			'admin/tinymce/tinymce.min.js',
			'admin/tinymce/tinymce_init.js',
		)

	list_display = ('id', 'name', 'timestamp', 'public',)
	list_display_links = ('id',)
	list_editable = ('name', 'public',)
	list_filter = ('public',)
	search_fields = ('name', 'studies', 'description',)
	filter_horizontal = ('partners',)
	prepopulated_fields = {'slug': ('name',)}


site.register(Programme, ProgrammeAdmin)
