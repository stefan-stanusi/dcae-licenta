#-*- coding: utf-8 -*-
"""
	DCAE - Partners - Admin:
		PartnerAdmin

	@author: mijomir mecu <self@mijomir.com>
"""
from django.contrib.admin.sites import site

from reversion import VersionAdmin

from .models import Partner


class PartnerAdmin(VersionAdmin):
	class Media:
		js = (
			'admin/tinymce/tinymce.min.js',
			'admin/tinymce/tinymce_init.js',
		)

	list_display = ('id', 'name', 'url', 'o', 'public',)
	list_display_links = ('id',)
	list_editable = ('url', 'o', 'public',)
	list_filter = ('public',)
	list_per_page = 20
	search_fields = ('name', 'description',)

site.register(Partner, PartnerAdmin)
