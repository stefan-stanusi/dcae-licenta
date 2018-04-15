#-*- coding: utf-8 -*-
"""
	DCAE - Members - Forms:
		MemberForm

	Defines a custom form to be used by members to update their info outside
	the admin website

	@author: mijomir mecu <self@mijomir.com>
"""
from django.forms import ModelForm

from .models import Member
from datatrans.models import KeyValue


class MemberForm(ModelForm):

	class Meta:
		model = Member


class TranslateForm(ModelForm):
	class Meta:
		model = KeyValue
