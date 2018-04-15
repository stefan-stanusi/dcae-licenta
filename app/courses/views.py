#-*- coding: utf-8 -*-
"""
	DCAE - Courses - Views

	@author: mijomir mecu <self@mijomir.com>
"""
from django.shortcuts import render
from django.http import Http404
from django.db.models import F

from .models import Course


def courses(request):
	courses = Course.objects.all().prefetch_related('m', 'r', 'coordinators',
		'people').filter(public=True)
	return render(request, 'courses/courses.html', {'courses': courses})


def course(request, pid, slug):
	courses = Course.objects.all().filter(public=True)
	try:
		c = courses.prefetch_related('m', 'r', 'coordinators',
		'people').get(pk=pid)
	except Course.DoesNotExist:
		raise Http404

	# update views; don't count logged in members' hits; or crawler hits
	user_agent = request.META.get('HTTP_USER_AGENT',None)
	Bots = ['AhrefsBot', 'org_bot', 'Baiduspider', 'BaiDuSpider', 'bingbot', 'cURL', 'Digg', 'DotBot', 'Facebot', 'Googlebot', 'googlebot', 'ia_archiver', 'Java', 'libwww-perl', 'magpie-crawler', 'Microsoft URL Control', 'MJ12bot', 'msnbot', 'Peach', 'PHP', 'PycURL', 'Python-urllib', 'SEOChat', 'SeznamBot', 'Slurp', 'Speedy', 'TweetedTimes', 'Wget', 'YandexBot', 'YandexImages']
	crawler = False

	for bot in Bots:
		if user_agent and bot in user_agent:
			crawler = True

	if not user_agent:
		crawler = True

	if not request.user.is_authenticated() and not crawler:
		cs = Course.objects.filter(pk=pid)
		cs.update(views=F('views')+1)

	return render(request, 'courses/course.html', {'c': c, 'courses': courses})
