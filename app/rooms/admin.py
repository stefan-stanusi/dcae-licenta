#-*- coding: utf-8 -*-
"""
	DCAE - Rooms - Admin:
		RoomAdmin

	@author: mijomir mecu <self@mijomir.com>
"""
from django.contrib.admin.sites import site
from reversion import VersionAdmin

from .models import Room


class RoomAdmin(VersionAdmin):
	list_display = ('id', 'name', 'timestamp', 'public',)
	list_display_links = ('id',)
	list_editable = ('name', 'public',)
	list_filter = ('public',)
	search_fields = ('name', 'description', )
	prepopulated_fields = {'slug': ('name',)}

site.register(Room, RoomAdmin)
