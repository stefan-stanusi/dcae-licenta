#-*- coding: utf-8 -*-
"""
	DCAE - Menu - Admin:
		MenuAdmin, MenuItem Inline

	@author: mijomir mecu <self@mijomir.com>
"""
from django.contrib.admin import StackedInline
from django.contrib.admin.sites import site

from singletons.admin import SingletonAdmin
from reversion import VersionAdmin

from .models import Menu, MenuItem


class MenuItemInline(StackedInline):
	model = MenuItem
	extra = 1
	max_num = 100
	classes = ('collapse closed',)
	inline_classes = ('collapse open',)


class MenuAdmin(SingletonAdmin, VersionAdmin):
	inlines = [MenuItemInline]


site.register(Menu, MenuAdmin)
