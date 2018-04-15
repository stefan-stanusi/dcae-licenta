#-*- coding: utf-8 -*-
"""
	DCAE - Publications - Views

	@author: mijomir mecu <self@mijomir.com>
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.template import loader, Context
from django.core.mail import mail_admins
from django.contrib.auth.models import User

from datatrans.utils import update_messages

from projects.models import Project
from members.models import Member
from .models import Genre, Publication
from .forms import PublicationForm


def publications(request):
	publications = Publication.objects.active().prefetch_related('gen', 'authors')

	return render(request, 'publications/publications.html',
		{'publications': publications})


def send_email_publication(pub):
	subject = u'New publication added/updated [dcae.pub.ro]'
	message = loader.get_template('publications/pub.txt').render(Context({'pub': pub}))

	mail_admins(subject, message)


@csrf_protect
@login_required
def publication(request):
	form = PublicationForm()
	genres = Genre.objects.all()
	members = Member.objects.active()

	if request.method == 'POST':
		form = PublicationForm(request.POST)
		if form.is_valid():
			form.clean()
			pub = form.save()
			pub.save()
			update_messages()
			send_email_publication(pub)
			return redirect('pubty')

	return render(request, 'publications/add.html', {'form': form, 'genres': genres, 'members': members})


@login_required
def pubty(request):
	return render(request, 'publications/pubty.html')


@csrf_protect
@login_required
def edit_publication(request, pid):

	p = Publication.objects.active().prefetch_related('gen',
		'authors').get(pk=pid)
	genres = Genre.objects.all()
	members = Member.objects.active()
	instance = get_object_or_404(Publication, id=pid)
	uu = request.user
	u = User.objects.get(pk=request.user.pk)
	try:
		m = Member.objects.active().get(u_id__exact=u)
	except Member.DoesNotExist:
		m = None

	if request.method == 'POST':
		form = PublicationForm(request.POST or None, instance=instance)
		if form.is_valid():
			form.clean()
			pub = form.save()
			pub.save()
			send_email_publication(pub)
			return redirect('pety')
	else:
		if m in p.authors.all() or uu.is_superuser:
			form = PublicationForm()
		else:
			form = None
			return redirect('publications')
		return render(request, 'publications/edit.html', {'p': p, 'form': form, 'genres': genres, 'members': members})

@login_required
def pety(request):
	return render(request, 'publications/pety.html')
