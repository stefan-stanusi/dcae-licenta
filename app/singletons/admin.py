#-*- coding: utf-8 -*-
"""
	DCAE - Singletons - Admin

	@author: mijomir mecu <self@mijomir.com>
"""
from django.contrib import admin
from django.conf.urls import url, patterns
from django.http import HttpResponseRedirect

from .models import Singleton

class SingletonAdmin(admin.ModelAdmin):
	# new templates
	object_history_template = "admin/singleton/object_history.html"
	change_form_template = "admin/singleton/change_form.html"

	# the model cannot accept another instance; and the single instance
	# cannot be deleted
	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False

	# appends to the default urls
	def get_urls(self):
		urls = super(SingletonAdmin, self).get_urls()
		url_name_prefix = '%(app_name)s_%(model_name)s' % {
			'app_name': self.model._meta.app_label,
			'model_name': self.model._meta.module_name,
			}
		custom_urls = patterns('',
			url(r'^history/$',
				self.admin_site.admin_view(self.history_view),
				{'object_id': '1'},
				name='%s_history' % url_name_prefix),
			url(r'^$',
				self.admin_site.admin_view(self.change_view),
				{'object_id': '1'},
				name='%s_change' % url_name_prefix),
		)
		return custom_urls + urls

	# modifying the edit page
	def response_change(self, request, obj):
		msg = u'%(obj)s was changed successfully.' % {'obj': obj}
		# save and add another button - redirect to the same page
		if '_continue' in request.POST:
			self.message_user(request, msg + ' ' + u'You may edit it again below.')
			return HttpResponseRedirect(request.path)
		# save button: redirect to admin homepage
		else:
			self.message_user(request, msg)
			return HttpResponseRedirect("../../")

	# always save or modify the unique instance
	def change_view(self, request, object_id, extra_context=None):
		if object_id == '1':
			self.model.objects.get_or_create(pk=1)
		return super(SingletonAdmin, self).change_view(
			request,
			object_id,
			extra_context=extra_context,
		)
