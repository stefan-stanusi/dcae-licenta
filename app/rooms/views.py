#-*- coding: utf-8 -*-
"""
	DCAE - Rooms - Views

	@author: mijomir mecu <self@mijomir.com>
"""
from django.shortcuts import render
from django.http import Http404

from .models import Room
from courses.models import Course
from labs.models import Laboratory


def rooms(request):
	rooms = Room.objects.all().prefetch_related('courses', 'members', 'labs'
		).filter(public=True)
	courses = Course.objects.all().filter(public=True).order_by('views', 'id')[:5]
	labs = Laboratory.objects.all().filter(public=True).order_by('views', 'id')[:5]

	return render(request, 'rooms/rooms.html',
		{'rooms': rooms, 'courses': courses, 'labs': labs})


def room(request, pid, slug):
	rooms = Room.objects.all().filter(public=True)
	try:
		r = rooms.prefetch_related('courses', 'members', 'labs').get(pk=pid)
	except Room.DoesNotExist:
		raise Http404
	courses = Course.objects.all().filter(public=True).order_by('views', 'id')[:5]
	labs = Laboratory.objects.all().filter(public=True).order_by('views', 'id')[:5]

	return render(request, 'rooms/room.html',
		{'r': r, 'courses': courses, 'labs': labs, 'rooms': rooms})
