#-*- coding: utf-8 -*-
"""
	DCAE - Search - Views:

	@author: mijomir mecu <self@mijomir.com>
"""
from django.shortcuts import render
from django.http import Http404

from announcements.models import Announcement
from courses.models import Course
from master.models import Programme
from members.models import Member
from projects.models import Project
from publications.models import Publication
from labs.models import Laboratory


def search(request):

	if 'q' in request.GET and request.GET['q']:
		query = request.GET['q']
	else:
		query = ''

	announcements = Announcement.search_objects.search(query, rank_field='rank')
	announcements = announcements.filter(public=True)

	courses = Course.search_objects.search(query, rank_field='rank')
	courses = courses.filter(public=True)

	programmes = Programme.search_objects.search(query, rank_field='rank')
	programmes = programmes.filter(public=True)

	members = Member.search_objects.search(query, rank_field='rank')
	members = members.filter(public=True)

	projects = Project.search_objects.search(query, rank_field='rank')
	projects = projects.filter(public=True)

	publications = Publication.search_objects.search(query, rank_field='rank')
	publications = publications.filter(public=True)

	labs = Laboratory.search_objects.search(query, rank_field='rank')
	labs = labs.filter(public=True)

	return render(request, 'search/search.html',
		{'query': query, 'announcements': announcements, 'courses': courses, 'members': members, 'projects': projects, 'publications': publications, 'labs': labs })
