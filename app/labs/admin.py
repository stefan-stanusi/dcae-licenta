#-*- coding: utf-8 -*-
"""
	DCAE - Labs - Admin:
		LaboratoryAdmin

	@author: mijomir mecu <self@mijomir.com>
"""
from django.contrib.admin.sites import site
from reversion import VersionAdmin

from .models import Laboratory

class LaboratoryAdmin(VersionAdmin):
	class Media:
		js = (
			'admin/tinymce/tinymce.min.js',
			'admin/tinymce/tinymce_init.js',
		)

	list_display = ('id', 'name', 'undergrad', 'views', 'timestamp', 'public',)
	list_display_links = ('id',)
	list_editable = ('name', 'undergrad', 'public',)
	list_filter = ('undergrad', 'public',)
	search_fields = ('name', 'description',)
	filter_horizontal = ('coordinators', 'people','r',)
	prepopulated_fields = {'slug': ('name',)}


site.register(Laboratory, LaboratoryAdmin)
