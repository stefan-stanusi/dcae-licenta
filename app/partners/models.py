#-*- coding: utf-8 -*-
"""
	DCAE - Partners - Models:
		Partner

	Defines a Partner model;
	objects can be deactivated/reactivated with a single click;
	translation support
	varoius versions of the object are stored in the database

	@todo:
		add image resize fields (sizes depend on frontend design)

		thumbnail = ImageSpecField(image_field='feat_image',
			processors=[ResizeToFit(1000, 350, white)])
		thumbnail_list = ImageSpecField(image_field='feat_image',
			processors=[ResizeToFit(300, 200, white)])

	@author: mijomir mecu <self@mijomir.com>
"""
from django.db.models import Model, CharField, URLField, TextField, \
	ImageField, BooleanField, SmallIntegerField
from django.utils.translation import ugettext_lazy as _

from datatrans.utils import register


class Partner(Model):
	name = CharField(max_length=255, db_index=True, help_text=_(u'Required \
		field, max 255 characters'))
	url = URLField(blank=True, max_length=255, help_text=_(u'Optional field, \
		max 255 characters'))
	logo = ImageField(upload_to='partners', help_text=_(u'Required field'))
	description = TextField(blank=True, help_text=_(u'Optional field'))
	o = SmallIntegerField(blank=True, null=True, verbose_name=u'Order',
		help_text=u'Optional field, only numeric values allowed. Sets the \
		ordering of the partners\' logos. If no value is provided, logos will\
		be ordered by their id, ascending.')
	public = BooleanField(default=False, db_index=True, help_text=_(u'Check \
		to display the partner\'s logo on the website. You can \
		deactivate/reactivate it at any time'))

	class Meta:
		verbose_name = u'Partner'
		verbose_name_plural = u'Partners'
		ordering = ('o', 'id',)

	def __unicode__(self):
		return u'%s' % self.name

	def save(self, *args, **kwargs):
		super(Partner, self).save(*args, **kwargs)
		if self.public is True:
			try:
				cache.delete('dcae_partners')
			except Exception, e:
				pass


class PartnerTranslation(object):
	fields = ('description',)

register(Partner, PartnerTranslation)
