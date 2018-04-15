#-*- coding: utf-8 -*-
"""
	DCAE - Announcements - Models:
		Announcement

	Defines an Announcement searchable model with a custom manager;
	objects can expire; they can also be published at specified times or
	deactivated/reactivated with a single click;
	translation support
	varoius versions of the object are stored in the database

	@author: mijomir mecu <self@mijomir.com>
"""
import logging
from datetime import datetime

from django.db.models import Manager, Q, CharField, SlugField, TextField, \
	ImageField, URLField, BooleanField, DateTimeField
from django.core.cache import cache
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from fts import SearchableModel, SearchManager
from imagekilt.models import ImageSpecField
from imagekilt.processors import ResizeToFit
from datatrans.utils import register

logger = logging.getLogger('app')


class AnnouncementsManager(Manager):
	# public announcements that aren't set to be published in the future and
	# haven't expired, i.e. the announcements to be publicly displayed
	def published(self):
		now = datetime.now()
		return self.active().filter(
			Q(expdate__isnull=True) | Q(expdate__gte=now), date__lte=now)

	# announcements that aren't just drafts
	def active(self):
		return super(AnnouncementsManager, self).get_query_set().filter(
			public=True)


class Announcement(SearchableModel):
	title = CharField(max_length=255, db_index=True, help_text=_(u'Max length \
		255 characters, required field.'))
	slug = SlugField(max_length=255, db_index=True, help_text=_(u'The \
		part of the URL specific to this announcement. This field is required; \
		it autocompletes from the value you enter in the title field, but you \
		can edit it to suit your need. Allowd characters: 0-9a-z-_ If the \
		field is left empty by the time you save the announcement, the slug \
		will be automatically generated.'))
	subtitle = CharField(max_length=255, blank=True, help_text=_(u'Optional \
		field, max lenght 255 characters.'))
	text = TextField(help_text=_(u'This field is required.'))
	image = ImageField(max_length=200, upload_to='announcements',
		blank=True, verbose_name=_(u'Main image'), help_text=_(u'Optional \
		field. allowed mime types: png, jpg, jpeg, gif.'))
	img_url = URLField(max_length=255, blank=True, verbose_name=_(u'Image URL'),
		help_text=_(u'Optionally, you can provide a URL for the image you want \
		to associate with the announcement. You need to supply the URL of the \
		image (something like http://example.com/image.jpg). It will be \
		downloaded and served from your server.'))
	thumbnail = ImageSpecField(image_field='image',
		processors=[ResizeToFit(220, 160)])
	evsdate = DateTimeField(blank=True, null=True, verbose_name=_(u'Event \
		starts'), help_text=_(u'Optional field'))
	evedate = DateTimeField(blank=True, null=True, verbose_name=_(u'Event \
		ends'), help_text=_(u'Optional field'))
	evlocation = CharField(blank=True, verbose_name=_(u'Event location'),
		help_text=_(u'Optional field, max 255 characters.'), max_length=255)
	summary = TextField(blank=True, help_text=_(u'An optional "tl;dr" \
		field. If filled, the template will output the value in a bold font, \
		above the text.'))
	metadescription = CharField(max_length=160, blank=True, help_text=_(u'\
		Optional field, max length 160 characters. Generates a metadescription \
		tag for search engines. If left blank, the meta tag will be filled \
		with the first 160 characters of the Text field.'))
	noindex = BooleanField(default=False, help_text=_(u'Check if you have \
		reasons to stop search engines from indexing this announcement.'))
	date = DateTimeField(default=datetime.now, db_index=True, verbose_name=_(u'\
		Publish date'), help_text=_('Announcement\'s publishing date and time, \
		defaults to now. If you set a future date, the announcement will be \
		published at that time.'))
	expdate = DateTimeField(blank=True, null=True, verbose_name=_(u'Expiration \
		date'), help_text=_(u'Optional field. If you set this date, the \
		announcement will become unavailble on the public section of the \
		website at that time.'))
	timestamp = DateTimeField(auto_now=True, db_index=True)
	public = BooleanField(default=False, help_text=_(u'Check this box \
		to make the announcement public. Uncheck if you need to stop it from \
		appearing on the website.'))

	objects = AnnouncementsManager()
	search_objects = SearchManager(fields=('title', 'subtitle', 'text',
		'summary',))


	class Meta:
		verbose_name = u'Announcement'
		verbose_name_plural = u'Announcements'
		ordering = ('-date', '-id')
		get_latest_by ='date'


	def __unicode__(self):
		return u'%s' % self.title


	def __init__(self, *args, **kwargs):
		super(Announcement, self).__init__(*args, **kwargs)

		# on init, previous and next announcements are unknown,
		# so they should default to None
		self._next = None
		self._prev = None


	def save(self, *args, **kwargs):
		# before save, make sure there is a slug
		if not self.slug:
			self.slug = slugify(self.title)

		# send data to the database
		super(Announcement, self).save(*args, **kwargs)

		# after save
		# invalidate cache (next/prev announcement, homepage announcements)
		if self.public is True:
			i = self.id
			keys = ('dcae_ann_%s' % i, 'dcae_anp_%s' % i, 'dcae_han')
			for key in keys:
				try:
					cache.delete(key)
				except Exception, e:
					logger.info(e)

		# now try retreive the remote image, if set and if no image has been
		# uploaded
		if self.img_url and not self.image:
			# first, check if the image has already been downloaded
			from django.conf import settings
			from utils.func import image_name_from_url, file_exists

			expected = '%s/announcements/%s' % (settings.MEDIA_ROOT,
				image_name_from_url(self.img_url))

			if file_exists(expected):
				pass # if the file has already been downloaded, execution stops here

			else: # image hasn't been downloaded yet

				# check if the provided url is an actual image
				from utils.func import is_url_image

				if is_url_image(self.img_url):
					# download file

					url = self.img_url
					path = '%s/announcements/%s' % (settings.MEDIA_ROOT,
						image_name_from_url(self.img_url))

					try:
						from urllib import urlretrieve
						urlretrieve(url, path)
					except Exception, e:
						logger.info(e)
				else:
					logger.info(u'The provided image URL for the Announcement "%s" was not a real image. Please check again.' % self.title)

	@property
	def metadesc(self):
		# builds a metadescription, if none provided
		if not self.metadescription:
			return u'%s' % self.text[:160]
		return None

	def is_modified(self):
		# checks if an announcement was modified since its creation
		if self.date < self.timestamp:
			return True
		return False
	is_modified.boolean = True

	@property
	def remote_image_url(self):
		# checks if the remote image has been properly downloaded before
		# trying to display it and stores the URL of the downloaded image
		if self.img_url and not self.image:
			key = 'dcae_an_%s_i' % self.id
			img = cache.get(key)

			# no value in cache
			if not img:
				from utils.func import file_exists, image_name_from_path,\
					image_name_from_url
				from django.conf import settings
				imgpath = '%s/announcements/%s' % (settings.MEDIA_ROOT,
						image_name_from_url(self.img_url))
				if file_exists(imgpath):
					img ='%s/announcements/%s' % (settings.MEDIA_URL,
						image_name_from_path(imgpath))
					cache.set(key, img, 900)
			return img
		return None

	@property
	def event_expired(self):
		if self.evedate:
			now = datetime.now()
			if now > self.evedate:
				return True
			return False


	def get_absolute_url(self):
		return '/anunturi/%s/%s/' % (self.id, self.slug)

	def get_next(self):
		# retreives the next announcement
		key = 'dcae_ann_%s' % self.id
		self._next = cache.get(key)
		# next announcement is not in memcache, let's hit the database
		if not self._next:
			try:
				qs = Announcement.objects.published().exclute(id__exact=self.id)
				announcement = qs.filter(date__gte=self.date).order_by('date')[0]
			except Announcement.DoesNotExist:
				announcement = None
			self._next = announcement
			# now store it in memcache
			cache.set(key, self._next, 900)

		return self._next

	def get_previous(self):
		# see get_next()
		key = 'dcae_anp_%s' % self.id
		self._prev = cache.get(key)

		if not self._prev:
			try:
				qs = Announcement.objects.published().exclute(id__exact=self.id)
				announcement = qs.filter(date__lte=self.date).order_by('-date')[0]
			except Announcement.DoesNotExist:
				announcement = None
			self._prev = announcement
			cache.set(key, self._prev, 900)

		return self._prev


class AnnouncementTranslation(object):
	fields = ('title', 'subtitle', 'text', 'summary', 'metadescription',)

register(Announcement, AnnouncementTranslation)
