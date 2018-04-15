#-*- coding: utf-8 -*-
"""
	DCAE - Homepage - Admin:
		InfoAdmin

	@author: mijomir mecu <self@mijomir.com>
"""
from django.contrib.admin.sites import site

from singletons.admin import SingletonAdmin
from reversion import VersionAdmin

from .models import Info

class InfoAdmin(SingletonAdmin, VersionAdmin):
	pass

site.register(Info, InfoAdmin)
