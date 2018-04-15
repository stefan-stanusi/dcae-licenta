#-*- coding: utf-8 -*-
"""
	DCAE - Projects - Models:
		Project

	@author: mijomir mecu <self@mijomir.com>
"""
from datetime import datetime

from django.db.models import CharField, SlugField, DateTimeField, \
	BooleanField, ManyToManyField, TextField, URLField
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from fts import SearchableModel, SearchManager
from datatrans.utils import register

from members.models import Member


class Project(SearchableModel):
	name = CharField(max_length=255, verbose_name=_(u'Name'), help_text=_(u'\
		Required field, max 255 characters'), db_index=True)
	slug = SlugField(db_index=True, max_length=255, help_text=_(u'Required \
		field. It autocompletes as you write the name. Edit only if necessary.'))
	description = TextField(blank=True, verbose_name=_(u'Description'),
		help_text=_(u'Optional field.'))
	url = URLField(max_length=255, verbose_name=_('Project\'s website'),
		blank=True, help_text=_(u'Required field, max 255 characters'))
	coordinators = ManyToManyField(Member, blank=True, null=True,
		verbose_name=_(u'Coordinators'), help_text=_(u'Please select from the \
		Department members list'), related_name='cprojects')
	people = ManyToManyField(Member, blank=True, null=True,
		verbose_name=_(u'Members involved'), help_text=_(u'Please select from \
		the Department members list'), related_name='pprojects')
	other = TextField(blank=True, verbose_name=_(u'Other people involved'),
		help_text=_(u'Optional field, e.g. Jane Doe, John Doe'))
	timestamp = DateTimeField(auto_now=True, db_index=True)
	public = BooleanField(default=False, help_text=_(u'Check to make the \
		research project visible on the website'))

	search_objects = SearchManager(fields=('name', 'description',))

	class Meta:
		verbose_name = _(u'Research project')
		verbose_name_plural = _(u'Research projects')
		ordering = ('name', 'id',)

	def __unicode__(self):
		return u'%s' % self.name


	def save(self, *args, **kwargs):
		# before save, make sure there is a slug
		if not self.slug:
			self.slug = slugify(self.name)

		# send data to the database
		super(Project, self).save(*args, **kwargs)


	def get_absolute_url(self):
		return '/proiecte/%s/%s/' % (self.id, self.slug)


class ProjectTranslation(object):
	fields = ('name', 'description',)


register(Project, ProjectTranslation)
