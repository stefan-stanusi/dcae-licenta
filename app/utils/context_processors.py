# -*- coding: utf-8 -*-
"""
Defines custom context processors:
	app_list, for building an admin menu

"""


from django.contrib.admin import site
from django.utils.text import capfirst
from django.db.models import get_models
from django.utils.safestring import mark_safe
from django.contrib.admin import ModelAdmin
from django.contrib.admin.validation import validate


def app_list(request):

	"""
	Builds an admin drop-down menu by getting all models and passing them
	to the context variable (apps)

	Source:
		http://smotko.si/navbar-in-django-admin/
	The original script, derived from Django's index view, displays all models,
	but it should skip the inlines, so we need to chek if the model is in the
	admin.site._registy dict
	"""

	user = request.user
	app_dict = {}
	admin_class = ModelAdmin

	# apps to be excluded from the navigation
	IGNORE_MODELS = (
		'sessions',
		'admin',
		'contenttypes',
		'sites',
		'south',
	)

	for model in get_models():

		# excluding the inline models
		if model in site._registry:

			validate(admin_class, model)
			model_admin = admin_class(model, None)
			app_label = model._meta.app_label

			if app_label in IGNORE_MODELS:
				continue

			has_module_perms = user.has_module_perms(app_label)

			if has_module_perms:
				perms = model_admin.get_model_perms(request)

				if True in perms.values():

					model_dict = {
						'name': capfirst(model._meta.verbose_name_plural),
						'admin_url': mark_safe('%s/%s/' % (app_label, model.__name__.lower())),
					}

					if app_label in app_dict:
						app_dict[app_label]['models'].append(model_dict)
					else:
						app_dict[app_label] = {
							'name': app_label.title(),
							'app_url': app_label + '/',
							'has_module_perms': has_module_perms,
							'models': [model_dict],
						}

	app_list = app_dict.values()
	app_list.sort(key=lambda x: x['name'])

	for app in app_list:
		app['models'].sort(key=lambda x: x['name'])

	return {'apps': app_list}
