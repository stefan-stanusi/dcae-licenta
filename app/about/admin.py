# -*- coding: utf-8 -*-
"""
	DCAE - About - Admin:
		AboutAdmin

	@author: mijomir mecu <self@mijomir.com>
"""
from django.contrib.admin.sites import site

from singletons.admin import SingletonAdmin
from reversion import VersionAdmin

from .models import About


class AboutAdmin(SingletonAdmin, VersionAdmin):
    # tinymce for textareas
    class Media:
        js = (
            'admin/tinymce/tinymce.min.js',
            'admin/tinymce/tinymce_init.js',
        )


site.register(About, AboutAdmin)
