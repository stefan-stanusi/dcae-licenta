#-*- coding: utf-8 -*-
"""
	DCAE - Projects - Views

	@author: mijomir mecu <self@mijomir.com>
"""
from django.shortcuts import render
from django.http import Http404

from .models import Project


def projects(request):
	projects = Project.objects.all().prefetch_related('coordinators', 'people'
		).filter(public=True)
	return render(request, 'projects/projects.html', {'projects': projects})


def project(request, pid, slug):
	projects = Project.objects.all().filter(public=True)
	try:
		p = projects.prefetch_related('coordinators', 'people'
		).filter(public=True).get(pk=pid)
	except Project.DoesNotExist:
		raise Http404
	return render(request, 'projects/project.html', {'p': p, 'projects': projects})
