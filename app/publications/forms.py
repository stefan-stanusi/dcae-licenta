#-*- coding: utf-8 -*-
"""
	DCAE - Publications - Forms:
		MemberForm

	Defines a custom form to be used by members to update their publications outside
	the admin website

	@author: mijomir mecu <self@mijomir.com>
"""
from django.forms import ModelForm

from .models import Publication


class PublicationForm(ModelForm):

	class Meta:
		model = Publication

	class Media:
		js = (
			'js/tinymce/tinymce.min.js',
			'js/tinymce/tinymce_init.js',
		)
