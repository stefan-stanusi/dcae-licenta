#-*- coding: utf-8 -*-
"""
	DCAE - Announcements - Views:
		announcement, announcements

	@author: mijomir mecu <self@mijomir.com>
"""
from datetime import datetime

from django.shortcuts import render
from django.http import Http404

from .models import Announcement


def announcement(request, pid, slug):
	try:
		a = Announcement.objects.published().get(pk=pid)
	except Announcement.DoesNotExist:
		raise Http404

	return render(request, 'announcements/announcement.html', {'a': a})


def announcements(request):
	announcements = Announcement.objects.published()
	return render(request, 'announcements/announcements.html',
		{'announcements': announcements})


def aarchive(request, year=None, month=None):
	# make sure month and year are integers
	year = int(year)
	month = int(month)

	announcements = Announcement.objects.published().select_related().filter(
		date__year=year, date__month=month)

	m = datetime(year, month, 1)

	return render(request, 'announcements/archive.html',
		{'announcements': announcements, 'm': m})
