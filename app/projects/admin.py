#-*- coding: utf-8 -*-
"""
	DCAE - Projects - Admin:
		ProjectAdmin

	@author: mijomir mecu <self@mijomir.com>
"""
from django.contrib.admin.sites import site
from reversion import VersionAdmin

from .models import Project


class ProjectAdmin(VersionAdmin):
	class Media:
		js = (
			'admin/tinymce/tinymce.min.js',
			'admin/tinymce/tinymce_init.js',
		)

	list_display = ('id', 'name', 'url', 'timestamp', 'public',)
	list_display_links = ('id',)
	list_editable = ('name', 'url', 'public',)
	list_filter = ('public',)
	search_fields = ('name', 'description',)
	filter_horizontal = ('coordinators', 'people',)
	prepopulated_fields = {'slug': ('name',)}


site.register(Project, ProjectAdmin)
