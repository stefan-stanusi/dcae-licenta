#-*- coding: utf-8 -*-
"""
	DCAE - Members - Models:
		Role, Member

	Defines a custom User profile.

	@author: mijomir mecu <self@mijomir.com>
"""
import logging
from datetime import datetime

from django.core.cache import cache
from django.db.models import Model, Manager, CharField, BooleanField, \
	ForeignKey, EmailField, TextField, ManyToManyField, SlugField, \
	IntegerField, SmallIntegerField, ImageField, URLField, DateTimeField
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from fts import SearchableModel, SearchManager
from imagekilt.models import ImageSpecField
from imagekilt.processors import SmartResize
from datatrans.utils import register

from rooms.models import Room


logger = logging.getLogger('apps')


class Role(Model):
	name = CharField(max_length=100, db_index=True, help_text=_(u'Required \
		field, max 100 characters. E.g. Profesori, Studenti'),
		verbose_name=_(u'Name'))
	singular_name = CharField(max_length=100, blank=True, verbose_name=_(u'\
		Singular name'), help_text=_(u'Optional field, max 100 characters. \
		E.g. Profesor, Student'))
	shortname = CharField(max_length=50, blank=True, verbose_name=_(u'Short \
		name'), help_text=_(u'Optional field, e.g. prof fro Professor. Used \
		in the listing page.'))
	description = TextField(blank=True, help_text=_(u'Optional field'),
		verbose_name=_(u'Description'))
	o = SmallIntegerField(blank=True, null=True, verbose_name=_(u'Order'),
		help_text=_(u'Optional field, only numeric values allowed. Defines the \
		order of the role in various pages.'))
	active = BooleanField(default=True, db_index=True, help_text=_(u'Uncheck \
		to deactivate this role. This should occur only in the event of \
		academic title changes.'), verbose_name=_(u'Active'))

	class Meta:
		verbose_name = _(u'Role')
		verbose_name_plural = _(u'Roles')
		ordering = ('o', 'id',)

	def __unicode__(self):
		return u'%s' % self.name


class MemberManager(Manager):

	def alumni(self):
		return self.active().filter(alumnus=True)

	def fmembers(self):
		return self.active().filter(faculty=True)

	def active(self):
		return super(MemberManager, self).get_query_set().filter(
			public=True)


class Member(SearchableModel):
	name = CharField(max_length=255, db_index=True, verbose_name=_(u'Last Name'),
		help_text=_(u'Required field, max 255 characters, used for listing'))
	first_name = CharField(blank=True, max_length=255, verbose_name=_(u'First \
		name'))
	slug = SlugField(db_index=True, max_length=255, help_text=_(u'Required \
		field. It autocompletes as you write the name. Edit only if necessary.'))
	u = ForeignKey(User, unique=True, default=0, verbose_name=_(u'User'),
		help_text=_(u'Members must be mapped to website\'s users. When tou \
		add a member, you have to create a user (just click on the green \
		"Plus" icon). This mapping ensures that members can only edit their \
		own info.'))
	r = ForeignKey(Role, related_name='members', verbose_name=_(u'Role'),
		help_text=_(u'Required field. If the role doesn\'t exist at the time \
		you add this member, click on the green "Plus" icon; a popup window \
		will open, and you\'ll be able to create the role.'))
	image = ImageField(max_length=200, upload_to='members', blank=True,
		verbose_name=_(u'Image'), help_text=_(u'Optional field. allowed mime \
		types: png, jpg, jpeg, gif. Recommended size is 220x200px, otherwise \
		the image will be resized (and cropped)'))
	thumbnail = ImageSpecField(image_field='image', processors=[SmartResize(220,
		250)])
	img_url = URLField(max_length=255, blank=True, verbose_name=_(u'Image URL'),
		help_text=_(u'Optionally, you can provide a URL for the image you want \
		to associate with the member. You need to supply the URL of the \
		image (something like http://example.com/image.jpg). It will be \
		downloaded and served from this server.'))
	phone = CharField(max_length=20, blank=True, verbose_name=_(u'Phone'),
		help_text=_(u'Optional field.'))
	email = EmailField(blank=True, max_length=254, verbose_name=_(u'Email'),
		help_text=u'Optional field, max 254 characterrs.')
	rm = ManyToManyField(Room, blank=True, null=True, verbose_name=_(u'Room'),
		help_text=_(u'Optional field'), related_name='members')
	coordinator = ManyToManyField('self', blank=True, null=True, help_text=_(u'\
		Optional field. Select this member\'s coordinator(s)'),
		symmetrical=False, related_name='coordinees')
	coord_bachelor = ManyToManyField('self', blank=True, null=True, help_text=_(u'\
		Optional field. Select the bachelor students coordinated by this member)'),
		verbose_name=_(u'Coordinated bachelor students'),
		symmetrical=False, related_name='mcoord_bachelor')
	coord_msc = ManyToManyField('self', blank=True, null=True, help_text=_(u'\
		Optional field. Select the MSc students coordinated by this member)'),
		verbose_name=_(u'Coordinated MSc students'),
		symmetrical=False, related_name='mcoord_msc')
	coord_phd = ManyToManyField('self', blank=True, null=True, help_text=_(u'\
		Optional field. Select the PHD students coordinated by this member)'),
		verbose_name=_(u'Coordinated PHD students'),
		symmetrical=False, related_name='mcoord_phd')
	degrees = TextField(blank=True, verbose_name=_(u'Academic degrees'),
		help_text=_(u'Optional field.'))
	experience = TextField(blank=True, verbose_name=_(u'Professional experience'),
		help_text=_(u'Optional field.'))
	activity = TextField(blank=True, verbose_name=_(u'Academic activity'),
		help_text=_(u'Optional field.'))
	notes = TextField(blank=True, verbose_name=_(u'Personal notes'),
		help_text=_(u'Required field'))
	alumnus = BooleanField(default=False, db_index=True, help_text=_(u'Optional \
		field.'))
	faculty = BooleanField(default=False, db_index=True, help_text=_(u'Optional \
		field.'), verbose_name=_(u'Faculty member'))
	attributions = TextField(blank=True, verbose_name=_(u'Attributions'),
		help_text=_(u'Optional field, for non faculty members; their \
		attributions in the department'))
	views = IntegerField(default=0, editable=False)
	timestamp = DateTimeField(auto_now=True, db_index=True)
	public = BooleanField(default=True, db_index=True, help_text=_(u'Uncheck \
		to deactivate this member. Inactive members shall not be displayed on \
		the website. If you uncheck this field, you must also inactivate the \
		website user corresponding to this member.'), verbose_name=_(u'Active'))

	objects = MemberManager()
	search_objects = SearchManager(fields=('name', 'degrees',
		'experience', 'activity', 'notes', 'first_name','attributions',))

	class Meta:
		verbose_name = _(u'Member')
		verbose_name_plural = _(u'Members')
		ordering = ('name', 'id',)

	def __unicode__(self):
		return u'%s' % self.get_full_name

	def save(self, *args, **kwargs):
		# before save, make sure there is a slug
		if not self.slug:
			self.slug = slugify(self.name)

		# send data to the database
		super(Member, self).save(*args, **kwargs)

		# after save
		# cache invalidation
		if self.public is True:
			key = 'dcae_m_%s_i' % self.id
			cache.delete(key)

		# try retreive the remote image, if set and if no image has been
		# uploaded
		if self.img_url and not self.image:
			# first, check if the image has already been downloaded
			from django.conf import settings
			from utils.func import image_name_from_url, file_exists

			expected = '%s/members/%s' % (settings.MEDIA_ROOT,
				image_name_from_url(self.img_url))

			if file_exists(expected):
				pass # if the file has already been downloaded, execution stops here

			else: # image hasn't been downloaded yet

				# check if the provided url is an actual image
				from utils.func import is_url_image

				if is_url_image(self.img_url):
					# download file
					url = self.img_url
					path = '%s/members/%s' % (settings.MEDIA_ROOT,
						image_name_from_url(self.img_url))

					try:
						from urllib import urlretrieve
						urlretrieve(url, path)
					except Exception, e:
						logger.info(e)
				else:
					logger.info(u'The provided image URL for the Member "%s" was not a real image. Please check again.' % self.name)

	@property
	def remote_image_url(self):
		# checks if the remote image has been properly downloaded before
		# trying to display it and stores the URL of the downloaded image
		key = 'dcae_m_%s_i' % self.id
		img = cache.get(key)

		if not img and not self.image and self.img_url:
			# no value in cache
			from utils.func import file_exists, image_name_from_path, \
					image_name_from_url
			from django.conf import settings
			imgpath = '%s/members/%s' % (settings.MEDIA_ROOT,
				image_name_from_url(self.img_url))
			if file_exists(imgpath):
				img ='%smembers/%s' % (settings.MEDIA_URL,
					image_name_from_path(imgpath))
				cache.set(key, img, 900)

		return img

	@property
	def get_full_name(self):
		return u'%s %s' % (self.first_name, self.name)

	def get_absolute_url(self):
		return '/membri/%s/%s/' % (self.id, self.slug)


class RoleTranslation(object):
	fields = ('name', 'shortname', 'description',)


class MemberTranslation(object):
	fields = ('degrees', 'experience', 'activity', 'notes', 'attributions')


register(Role, RoleTranslation)
register(Member, MemberTranslation)
