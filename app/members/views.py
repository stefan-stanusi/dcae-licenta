#-*- coding: utf-8 -*-
"""
	DCAE - Members - Views

	@author: mijomir mecu <self@mijomir.com>
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import F, Q
from django.contrib.contenttypes.models import ContentType

from datatrans.models import KeyValue
from datatrans.utils import update_messages, find_obsoletes, \
	get_default_language
from homepage.models import Info

from .models import Role, Member
from .forms import MemberForm, TranslateForm


def members(request):
	roles = Role.objects.all().prefetch_related('members').filter(active=True)
	members = Member.objects.active().prefetch_related('rm', 'ccourses'
		).order_by('name', 'id')

	return render(request, 'members/members.html',
		{'roles': roles, 'mbs': members})


def member(request, pid, slug):

	members = Member.objects.active().order_by('name', 'id')

	try:
		m = members.prefetch_related('u', 'r', 'coordinator', 'coordinees',
			'coord_bachelor', 'mcoord_bachelor', 'coord_msc', 'coord_phd',
			'mcoord_phd', 'ccourses', 'pcourses', 'clabs', 'plabs',
			'cprojects', 'pprojects', 'mpublications').get(pk=pid)
	except Member.DoesNotExist:
		raise Http404

	try:
		i = Info.objects.get(pk=1)
	except Info.DoesNotExist:
		i = None

	# update views; don't count members' own hits; or crawler hits
	if request.user.is_authenticated():
		#user = User.objects.get(pk=request.user.pk)
		p = request.user.pk
	else:
		p = 0

	user_agent = request.META.get('HTTP_USER_AGENT', None)
	Bots = ['AhrefsBot', 'org_bot', 'Baiduspider', 'BaiDuSpider', 'bingbot',
	'cURL', 'Digg', 'DotBot', 'Facebot', 'Googlebot', 'googlebot',
	'ia_archiver', 'Java', 'libwww-perl', 'magpie-crawler',
	'Microsoft URL Control', 'MJ12bot', 'msnbot', 'Peach', 'PHP', 'PycURL',
	'Python-urllib', 'SEOChat', 'SeznamBot', 'Slurp', 'Speedy', 'TweetedTimes',
	'Wget', 'YandexBot', 'YandexImages']
	crawler = False

	for bot in Bots:
		if user_agent and bot in user_agent:
			crawler = True

	if not user_agent:
		crawler = True

	if m and not crawler and p != m.u.pk:
		mb = Member.objects.filter(pk=pid)
		mb.update(views=F('views')+1)

	return render(request, 'members/member.html',
		{'m': m, 'mbs': members, 'i': i})


@csrf_protect
@login_required
def profile(request):
	# get the user ID; None, if user is not logged in
	#u = User.objects.get(pk=request.user.pk)
	form = MemberForm()

	try:
		m = Member.objects.active().prefetch_related('u', 'r', 'coordinator',
			'coord_bachelor', 'coord_msc', 'mcoord_msc',
			'coord_phd').get(u_id__exact=request.user.pk)
	except Member.DoesNotExist:
		raise Http404

	instance = get_object_or_404(Member, id=m.id)

	ct = ContentType.objects.get(model='member')
	ct = ct.id

	lang = request.LANGUAGE_CODE

	degrees = KeyValue.objects.all().filter(content_type=ct, field='degrees',
		object_id=m.id, language=lang)
	degrees = degrees[0]
	experience = KeyValue.objects.all().filter(content_type=ct, field='experience',
		object_id=m.id, language=lang)
	experience = experience[0]
	activity = KeyValue.objects.all().filter(content_type=ct, field='activity',
		object_id=m.id, language=lang)
	activity = activity[0]
	notes = KeyValue.objects.all().filter(content_type=ct, field='notes',
		object_id=m.id, language=lang)
	notes = notes[0]

	all_obsoletes = find_obsoletes().order_by('digest')
	obsoletes = all_obsoletes.filter(Q(edited=True) | Q(language=get_default_language()))

	if request.method == 'POST':
		form = MemberForm(request.POST or None, request.FILES or None, instance=instance)
		if form.is_valid():
			form.clean()
			details = form.save()
			details.save()
			degrees.save()
			experience.save()
			activity.save()
			notes.save()
			obsoletes.delete()
			update_messages()
			return redirect('pty')

	return render(request, 'members/profile.html', {'user': request.user, 'm': m, 'form': form})


@login_required
def pty(request):
	return render(request, 'members/pty.html')


@csrf_protect
@login_required
def translate_degrees(request):
	# get the user ID; None, if user is not logged in
	u = User.objects.get(pk=request.user.pk)
	try:
		m = Member.objects.active().get(u_id__exact=u)
	except Member.DoesNotExist:
		raise Http404

	user = request.user
	perms = user.has_perm('datatrans.change_keyvalue')
	form = TranslateForm()
	ct = ContentType.objects.get(model='member')
	ct = ct.id
	formdata = KeyValue.objects.all().filter(content_type=ct, field='degrees',
		object_id=m.id, language='ro')
	formdata = formdata[0]
	instance = get_object_or_404(KeyValue, id=formdata.id)

	degrees = KeyValue.objects.all().filter(content_type=ct, field='degrees',
		object_id=m.id, language='en')
	degrees = degrees[0]

	if request.method == 'POST':
		form = TranslateForm(request.POST or None, instance=formdata)
		if form.is_valid():
			form.clean()
			trans = form.save()
			trans.save()
			return redirect('transty')

	return render(request, 'members/translate/degrees.html',
			{'user': user, 'm': m, 'form': form, 'ct': ct, 'perms': perms,
			'formdata': formdata, 'degrees': degrees})


@csrf_protect
@login_required
def translate_experience(request):
	# get the user ID; None, if user is not logged in
	u = User.objects.get(pk=request.user.pk)

	try:
		m = Member.objects.active().get(u_id__exact=u)
	except Member.DoesNotExist:
		raise Http404

	user = request.user
	perms = user.has_perm('datatrans.change_keyvalue')
	form = TranslateForm()
	ct = ContentType.objects.get(model='member')
	ct = ct.id
	formdata = KeyValue.objects.all().filter(content_type=ct,
		field='experience', object_id=m.id, language='ro')
	formdata = formdata[0]

	experience = KeyValue.objects.all().filter(content_type=ct, field='experience',
		object_id=m.id, language='en')
	experience = experience[0]

	if request.method == 'POST':
		form = TranslateForm(request.POST or None, instance=formdata)
		if form.is_valid():
			form.clean()
			trans = form.save()
			trans.save()
			return redirect('transty')

	return render(request, 'members/translate/experience.html',
			{'user': user, 'm': m, 'form': form, 'ct': ct, 'perms': perms,
			'formdata': formdata, 'experience': experience})


@csrf_protect
@login_required
def translate_activity(request):
	# get the user ID; None, if user is not logged in
	u = User.objects.get(pk=request.user.pk)

	try:
		m = Member.objects.active().get(u_id__exact=u)
	except Member.DoesNotExist:
		raise Http404

	user = request.user
	perms = user.has_perm('datatrans.change_keyvalue')
	form = TranslateForm()
	ct = ContentType.objects.get(model='member')
	ct = ct.id
	formdata = KeyValue.objects.all().filter(content_type=ct, field='activity',
		object_id=m.id, language='ro')
	formdata = formdata[0]

	activity = KeyValue.objects.all().filter(content_type=ct, field='activity',
		object_id=m.id, language='en')
	activity = activity[0]

	if request.method == 'POST':
		form = TranslateForm(request.POST or None, instance=formdata)
		if form.is_valid():
			form.clean()
			trans = form.save()
			trans.save()
			return redirect('transty')

	return render(request, 'members/translate/activity.html',
		{'user': user, 'm': m, 'form': form, 'ct': ct, 'perms': perms,
		'formdata': formdata, 'activity': activity})

@csrf_protect
@login_required
def translate_notes(request):
	# get the user ID; None, if user is not logged in
	u = User.objects.get(pk=request.user.pk)

	try:
		m = Member.objects.active().get(u_id__exact=u)
	except Member.DoesNotExist:
		raise Http404

	user = request.user
	perms = user.has_perm('datatrans.change_keyvalue')
	form = TranslateForm()
	ct = ContentType.objects.get(model='member')
	ct = ct.id
	formdata = KeyValue.objects.all().filter(content_type=ct, field='notes',
		object_id=m.id, language='ro')
	formdata = formdata[0]

	notes = KeyValue.objects.all().filter(content_type=ct, field='notes',
		object_id=m.id, language='en')
	notes = notes[0]

	if request.method == 'POST':
		form = TranslateForm(request.POST or None, instance=formdata)
		if form.is_valid():
			form.clean()
			trans = form.save()
			trans.save()
			return redirect('transty')


	return render(request, 'members/translate/notes.html',
			{'user': user, 'm': m, 'form': form, 'ct': ct, 'perms': perms,
			'formdata': formdata, 'notes': notes})


@login_required
def transty(request):
	return render(request, 'members/translate/transty.html')
