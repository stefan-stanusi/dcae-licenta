# -*- coding: utf-8 -*-
"""
	DCAE - About - Views

	@author: mijomir mecu <self@mijomir.com>
"""
from django.shortcuts import render

from .models import About


def about(request):
    try:
        d = About.objects.get(pk=1)
    except About.DoesNotExist:
        d = None

    return render(request, 'about/about.html', {'d': d})
