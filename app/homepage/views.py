#-*- coding: utf-8 -*-
"""
	DCAE - Homepage - Views

	@author: mijomir mecu <self@mijomir.com>
"""
from django.shortcuts import render

from .models import Info
from members.models import Member
from announcements.models import Announcement
from master.models import Programme
from courses.models import Course
from labs.models import Laboratory


def homepage(request):
	try:
		i = Info.objects.get(pk=1)
	except Info.DoesNotExist:
		i = None
	members = Member.objects.fmembers().order_by('-views', 'id')[:4]
	announcements = Announcement.objects.published()[:4]
	masters = Programme.objects.all().filter(public=True).order_by('-views', 'id')[:4]
	courses = Course.objects.all().filter(public=True).order_by('-views', 'id')[:2]
	labs = Laboratory.objects.all().filter(public=True).order_by('-views', 'id')[:2]

	return render(request, 'homepage/homepage.html', {'i': i, 'members': members, 'announcements': announcements, 'masters': masters, 'courses': courses, 'labs': labs})
