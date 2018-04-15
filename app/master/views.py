#-*- coding: utf-8 -*-
"""
	DCAE - Master - Views

	@author: mijomir mecu <self@mijomir.com>
"""
from django.shortcuts import render
from django.http import Http404
from django.db.models import F

from .models import Programme


def masters(request):
	masters = Programme.objects.all().prefetch_related('partners').filter(
		public=True)
	return render(request, 'master/masters.html', {'masters': masters})


def master(request, pid, slug):
	masters = Programme.objects.all().filter(public=True)
	try:
		m = masters.prefetch_related('partners', 'mcourses', 'mlabs').get(pk=pid)
	except Programme.DoesNotExist:
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
		ms = Programme.objects.filter(pk=pid)
		ms.update(views=F('views')+1)

	return render(request, 'master/master.html', {'m': m, 'masters': masters})
