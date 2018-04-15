#-*- coding: utf-8 -*-
"""
	DCAE - Courses - Models:
		Course

	@author: mijomir mecu <self@mijomir.com>
"""
from datetime import datetime

from django.db.models import CharField, ForeignKey, TextField, DateTimeField, \
	BooleanField, SlugField, IntegerField, ManyToManyField, URLField
from django.utils.translation import ugettext_lazy as _

from fts import SearchableModel, SearchManager
from datatrans.utils import register

from members.models import Member
from master.models import Programme
from rooms.models import Room


class Course(SearchableModel):
	name = CharField(max_length=255, db_index=True, verbose_name=_(u'Course'),
		help_text=_(u'Required field, max 255 characters.'))
	slug = SlugField(db_index=True, max_length=255, help_text=_(u'Required \
		field. It autocompletes as you write the name. Edit only if necessary.'))
	m = ForeignKey(Programme, blank=True, null=True, verbose_name=_(u'Master'),
		help_text=_(u'Optional field'), related_name='mcourses')
	undergrad = BooleanField(default=False, db_index=True, verbose_name=_(u'\
		Undergraduate curriculum'), help_text=_(u'Check if the course does not \
		belong to a master programme.'))
	r = ManyToManyField(Room, blank=True, null=True, verbose_name=_(u'Rooms'),
		help_text=_(u'Optional field, the rooms where this course is being \
		taught'), related_name='courses')
	coordinators = ManyToManyField(Member, blank=True, null=True,
		verbose_name=_(u'Coordinators'), help_text=_(u'Please select from the \
		Department members list'), related_name='ccourses')
	people = ManyToManyField(Member, blank=True, null=True,
		verbose_name=_(u'Members involved'), help_text=_(u'Please select from \
		the Department members list'), related_name='pcourses')
	url = URLField(max_length=255, verbose_name=_('Link to the course support'),
		blank=True, help_text=_(u'Optional field, max 255 characters'))
	ro_url = URLField(max_length=255, verbose_name=_('Link to the lab support,\
		romanian version'), blank=True,
		help_text=_(u'Optional field, max 255 characters'))
	description = TextField(blank=True, help_text=_(u'Optional field'),
		verbose_name=_(u'Description'))
	timestamp = DateTimeField(auto_now=True, db_index=True)
	views = IntegerField(default=0, editable=False)
	public = BooleanField(default=False, help_text=_(u'Check to make the \
		course visible on the website'))

	search_objects = SearchManager(fields=('name', 'description',))

	class Meta:
		verbose_name = _(u'Course')
		verbose_name_plural = _(u'Courses')
		ordering = ('name', 'id',)

	def __unicode__(self):
		return u'%s' % self.name


	def save(self, *args, **kwargs):
		# before save, make sure there is a slug
		if not self.slug:
			self.slug = slugify(self.name)

		# send data to the database
		super(Course, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return '/cursuri/%s/%s/' % (self.id, self.slug)


class CourseTranslation(object):
	fields = ('name', 'description',)


register(Course, CourseTranslation)
