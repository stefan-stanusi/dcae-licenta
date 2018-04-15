# -*- coding: utf-8 -*-
"""
	DCAE - About - Models:
		About

	Defines a singleton model allowing admins to edit the About Page

	@author: mijomir mecu <self@mijomir.com>
"""
from datetime import datetime

from django.db.models import CharField, TextField, ImageField, DateTimeField
from django.utils.translation import ugettext_lazy as _

from singletons.models import Singleton
from datatrans.utils import register


class About(Singleton):
    title = CharField(max_length=100, db_index=True, default=u'About Us',
                      help_text=_(u'Required Field, max 100 characters'))
    image = ImageField(max_length=200, upload_to='about', blank=True,
                       help_text=_(u'Optional field. allowed mime types: png, jpg, jpeg, gif.'))
    text = TextField(help_text=_(u'Required field'))
    edited = DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = u'About'
        verbose_name_plural = u'About'
        ordering = ('id',)

    def __unicode__(self):
        return u'About'


class AboutTranslation(object):
    fields = ('title', 'text',)


register(About, AboutTranslation)
