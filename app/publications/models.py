# -*- coding: utf-8 -*-
"""
	DCAE - Publications - Models:
		Genre, Publication

	@author: mijomir mecu <self@mijomir.com>
"""
from datetime import datetime

from django.db.models import Model, CharField, DateTimeField, ManyToManyField, \
    TextField, SmallIntegerField, URLField, BooleanField, ForeignKey, Manager
from django.utils.translation import ugettext_lazy as _

from fts import SearchableModel, SearchManager
from datatrans.utils import register

from members.models import Member


class Genre(Model):
    name = CharField(max_length=100, db_index=True, verbose_name=_(u'Type'),
                     help_text=_(u'Required field, max 100 characters. E.g. Bachelor/ Msc./ \
		Ph.D Thesis/ Journal / Conference'))
    description = TextField(blank=True, help_text=_(u'Optional field'),
                            verbose_name=_(u'Description'))
    timestamp = DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = _(u'Genre')
        verbose_name_plural = _(u'Genres')
        ordering = ('name', 'id',)

    def __unicode__(self):
        return u'%s' % self.name


class PublicationManager(Manager):
    def active(self):
        return super(PublicationManager, self).get_query_set().filter(
            public=True)


class Publication(SearchableModel):
    gen = ForeignKey(Genre, blank=True, null=True, verbose_name=_(u'Type'))
    authors = ManyToManyField(Member, blank=True, null=True, verbose_name=_(u'\
		Authors'), related_name='mpublications',
                              help_text=_(u'Please select from the Department members list'))
    oauthors = TextField(blank=True, verbose_name=_(u'Other authors'),
                         help_text=_(u'Optional field, in case some of the authors are not \
		members of the department, e.g. DOE, John, DOE, Jane'))
    title = TextField(verbose_name=_(u'Title'), help_text=u'Required field')
    publisher = CharField(max_length=255, blank=True, verbose_name=u'\
		Publishing house', help_text=_(u'Optional field.'))
    city = CharField(max_length=255, blank=True, verbose_name=_(u'City'),
                     help_text=_(u'Optional field.'))
    review = TextField(blank=True, verbose_name=_(u'Review info'),
                       help_text=_(u'Optional field. Please fill pages and year below.'))
    conference = TextField(blank=True, verbose_name=_(u'Conference info'),
                           help_text=_(u'Optional field.  Please fill pages and year below.'))
    other = TextField(blank=True, verbose_name=_(u'Other info'),
                      help_text=_(u'Optional field.'))
    pp = CharField(max_length=100, blank=True, verbose_name=_(u'Pages'),
                   help_text=_(u'Optional fiels, eg. 127-152'))
    year = SmallIntegerField(max_length=4, verbose_name=_(u'Year'),
                             help_text=_(u'Required field.'))
    book = BooleanField(default=False, help_text=_(u'Check if the publication \
		is a book; important for formatting.'), verbose_name=_(u'The \
		publication is a book.'))
    abstract = TextField(blank=True, help_text=_(u'Optional field'),
                         verbose_name=_(u'Abstract'))
    url = URLField(max_length=255, verbose_name=_('Link to the document'),
                   blank=True, help_text=_(u'Optional field, max 255 characters'))
    timestamp = DateTimeField(auto_now=True, db_index=True)
    public = BooleanField(default=False, help_text=_(u'Check to make the \
		publication visible on the website'))

    objects = PublicationManager()
    search_objects = SearchManager(fields=('title', 'oauthors', 'publisher',
                                           'city', 'review', 'conference', 'other', 'abstract',))

    class Meta:
        verbose_name = _(u'Publication')
        verbose_name_plural = _(u'Publications')
        ordering = ('year', 'title',)
        get_latest_by = 'timestamp'

    def __unicode__(self):
        return u'%s' % self.title


class GenreTranslation(object):
    fields = ('name', 'description',)


class PublicationTranslation(object):
    fields = ('abstract',)


register(Genre, GenreTranslation)
register(Publication, PublicationTranslation)
