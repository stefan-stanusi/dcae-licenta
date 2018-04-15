#-*- coding: utf-8 -*-
"""
	DCAE - Members - Admin:
		RoleAdmin, MembersAdmin

	@author: mijomir mecu <self@mijomir.com>
"""
from django.contrib.admin.sites import site
from reversion import VersionAdmin

from .models import Role, Member


class RoleAdmin(VersionAdmin):
	list_display = ('id', 'name', 'shortname', 'o', 'active',)
	list_display_links = ('id',)
	list_editable = ('name', 'shortname', 'o', 'active',)
	list_filter = ('active',)
	search_fields = ('name', 'shortname',)


class MemberAdmin(VersionAdmin):
	list_display = ('id', 'first_name', 'name', 'r', 'faculty', 'alumnus',
		'views', 'public',)
	list_display_links = ('id',)
	list_editable = ('faculty', 'alumnus', 'public',)
	list_filter = ('r', 'alumnus', 'public',)
	search_fields = ('first_name', 'name', 'degrees', 'experience',
		'activity', 'notes',)
	filter_horizontal = ('coordinator', 'coord_bachelor', 'coord_msc',
		'coord_phd', 'rm',)
	prepopulated_fields = {'slug': ('name',)}


site.register(Role, RoleAdmin)
site.register(Member, MemberAdmin)
