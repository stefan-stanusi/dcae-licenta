#-*- coding: utf-8 -*-
"""
	DCAE - Announcements - Admin:
		AnnouncementAdmin

	@author: mijomir mecu <self@mijomir.com>
"""
from django.contrib.admin.sites import site

from reversion import VersionAdmin

from .models import Announcement


class AnnouncementAdmin(VersionAdmin):
	class Media:
		js = (
			'admin/tinymce/tinymce.min.js',
			'admin/tinymce/tinymce_init.js',
		)

	list_display = ('id', 'title', 'evsdate', 'evedate', 'date', 'expdate', 'public',)
	list_display_links = ('id',)
	list_editable = ('title', 'evsdate', 'evedate', 'date', 'expdate', 'public',)
	list_filter = ('public',)
	list_per_page = 20
	search_fields = ('title', 'subtitle', 'summary', 'text',)

	prepopulated_fields = {'slug': ('title',)}

site.register(Announcement, AnnouncementAdmin)
