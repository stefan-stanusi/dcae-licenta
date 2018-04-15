#-*- coding: utf-8 -*-
"""
	DCAE - Master - Models:
		Programme

	@author: mijomir mecu <self@mijomir.com>
"""
from datetime import datetime

from django.db.models import CharField, TextField, ManyToManyField, \
	DateTimeField, BooleanField, SlugField, IntegerField
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from fts import SearchableModel, SearchManager
from datatrans.utils import register

from partners.models import Partner


class Programme(SearchableModel):
	name = CharField(max_length=255, verbose_name=_(u'Name'), help_text=_(u'\
		Required field, max 255 characters'), db_index=True)
	slug = SlugField(db_index=True, max_length=255, help_text=_(u'Required \
		field. It autocompletes as you write the name. Edit only if necessary.'))
	studies = TextField(blank=True, verbose_name=_(u'Directions of study'),
		help_text=_(u'Optional field.'))
	description = TextField(blank=True, verbose_name=_(u'Description'),
		help_text=_(u'Optional field.'))
	partners = ManyToManyField(Partner, blank=True, null=True,
		verbose_name=_(u'Partners'), help_text=_(u'Optional field.'))
	timestamp = DateTimeField(auto_now=True, db_index=True)
	views = IntegerField(default=0, editable=False)
	public = BooleanField(default=False, help_text=_(u'Check to make the \
		master programme visible on the website'))

	search_objects = SearchManager(fields=('name', 'studies', 'description',))

	class Meta:
		verbose_name = _(u'Master programme')
		verbose_name_plural = _(u'Master programmes')
		ordering = ('name', 'id',)

	def __unicode__(self):
		return u'%s' % self.name


	def save(self, *args, **kwargs):
		# before save, make sure there is a slug
		if not self.slug:
			self.slug = slugify(self.name)

		# send data to the database
		super(Programme, self).save(*args, **kwargs)


	def get_absolute_url(self):
		return '/master/%s/%s/' % (self.id, self.slug)


class ProgrammeTranslation(object):
	fields = ('name', 'studies', 'description',)


register(Programme, ProgrammeTranslation)
