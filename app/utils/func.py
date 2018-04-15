#-*- coding: utf-8 -*-
"""
	DCAE - Utils - Func

	Small useful functions and helpers
	@author: mijomir mecu <self@mijomir.com>
"""

from urlparse import urlparse
from os.path import basename, splitext, isfile
import mimetypes



def is_url_image(url):
	mimetype = mimetypes.guess_type(url)
	if mimetype and mimetype[0] and mimetype[0].startswith('image'):
		return True
	return False


def image_name_from_url(url):
	parsed = urlparse(url)
	filename, file_ext = splitext(basename(parsed.path))
	fname = '%s%s' % (filename, file_ext)

	return fname


def image_name_from_path(p):
	filename, file_ext = splitext(basename(p))
	fname = '%s%s' % (filename, file_ext)

	return fname


def file_exists(f):
	return isfile(f)
