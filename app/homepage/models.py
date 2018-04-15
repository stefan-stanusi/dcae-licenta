#-*- coding: utf-8 -*-
"""
	DCAE - Homepage - Models:
		Info

	Defines a singleton model allowing admins to edit the About Page

	@author: mijomir mecu <self@mijomir.com>
"""
from datetime import datetime

from django.db.models import CharField, TextField, URLField, ImageField, \
	EmailField
from django.utils.translation import ugettext_lazy as _

from singletons.models import Singleton
from datatrans.utils import register


class Info(Singleton):
	title = CharField(max_length=100, db_index=True, verbose_name=_(u'\
		Freatured area title'), default='Dispozitive, Circuite si Arhitecturi Electronice',
		help_text=_(u'Required field, max 100 characters. The \
		following fields represent a mechanism to easily signaling something \
		important on the front page in the featured turqoise area. You can \
		revert to previous version of the info at any time.'))
	text = TextField(blank=True, help_text=_(u'Optional field, a few words \
		describing the Department. HTML, please.'))
	anchor_text = CharField(max_length=40, default=u'Citeste mai multe despre noi',
		blank=True, verbose_name=_(u'Anchor text'), help_text=_(u'Displayed on \
		the red button'))
	anchor_url = URLField(blank=True, max_length=255, verbose_name=_(u'Anchor \
		URL'), help_text=_(u'The red button points to this page.'))
	image = ImageField(upload_to='homepage', blank=True, verbose_name=_(u'\
		Featured image'), help_text=_(u'If you need to change the default \
		background image of the featured turquoise area, you need to make sure \
		it blends; the default background color code is #00868b. Optional \
		field.'))
	image_ro = ImageField(upload_to='homepage', blank=True, verbose_name=_(u'\
		Ro featured image'), help_text=_(u'If you need to change the default \
		background image of the featured turquoise area, you need to make sure \
		it blends; the default background color code is #00868b. Optional \
		field.'), default='/static/img/home_lead.jpg')
	bg = CharField(blank=True, max_length=30, default='#00868b',
		verbose_name=_(u'Background color'), help_text=_(u'You can change the \
		turqoise background of the featured area. Hexadecimal or RGB(A) \
		values, eg. #00868b || rgb(1, 134, 139) || rgba(255, 255, 255, 0.5)'))
	logo = ImageField(upload_to='homepage', blank=True, verbose_name=_(u'Top \
		logos'), help_text=_(u'Optional field, in case you need to change the \
		logos in the featured area. Transparent PNG recommended.'))
	logo_ro = ImageField(upload_to='homepage', blank=True, verbose_name=_(u'Top \
		logos, ro version'), help_text=_(u'Optional field, in case you need to \
		change the logos in the featured area. Transparent PNG recommended.'),
		default='/static/img/home_logos.png')
	rapid_access = CharField(blank=True, default='Acces rapid', max_length=100,
		help_text=_(u'Optional field'))
	study_programs = CharField(blank=True, default='Programe de studiu',
		max_length=100, help_text=_(u'Optional field'))
	faculty = CharField(blank=True, default='Cadre didactice', max_length=100,
		help_text=_(u'Optional field'))
	resources = CharField(blank=True, default='Resurse / Suport cursuri',
		max_length=100, help_text=_(u'Optional field'))
	news = CharField(blank=True, default='Stiri / noutati', max_length=100,
		help_text=_(u'Optional field'))
	twitter = TextField(blank=True, verbose_name=_(u'Twitter widget code'),
		help_text=_(u'Optional field'))
	gc = TextField(blank=True, verbose_name=_(u'Google Calendar code'),
		help_text=_(u'Optional field'))
	address = TextField(blank=True, default=u'<p>Complex LEU<br>Bd. Iuliu \
		Maniu, nr. 1-3<br>Sect. 6, 061071, Bucuresti, Romania</p>',
		verbose_name=_(u'Address'), help_text=_(u'Optional field'))
	phone = CharField(max_length=20, blank=True, verbose_name=_(u'Phone'),
		help_text=_(u'Optional field, department\'s phone'))
	email = EmailField(blank=True, max_length=254, help_text=_(u'Optional \
		field'))

	class Meta:
		verbose_name = _(u'Homepage Info')
		verbose_name_plural = _(u'Homepage Info')
		ordering = ('id',)

	def __unicode__(self):
		return u'Homepage Info'


class InfoTranslation(object):
	fields = ('title', 'text', 'anchor_text', 'rapid_access', 'study_programs',
		'faculty', 'resources', 'news', 'address')

register(Info, InfoTranslation)
