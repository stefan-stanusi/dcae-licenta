#-*- coding: utf-8 -*-
"""
	DCAE - Members - Templatetags
	Maps members to site users

	@author: mijomir mecu <self@mijomir.com>
"""
import re

from django import template
from django.template import RequestContext

from django.contrib.auth.models import User
from members.models import Member

register = template.Library()

class GetMemberInfoNode(template.Node):

	def __init__(self, varname):
		self.varname = varname

	def render(self, context):
		us = context['request'].user
		u = User.objects.all().get(pk=us.id)
		try:
			m = Member.objects.active().get(u_id__exact=u)
		except Member.DoesNotExist:
			m = None

		context[self.varname] = m
		return ''

def get_member_info(parser, token):
	args = token.split_contents()
	argc = len(args)

	try:
		assert argc == 3 and args[1] == 'as'
	except AssertionError:
		raise template.TemplateSyntaxError('get_member_info syntax: {% get_member_info as varname %}')

	return GetMemberInfoNode(args[2])


class EncryptEmail(template.Node):

	def __init__(self, context_var):
		self.context_var = template.Variable(context_var)

	def render(self, context):
		import random

		email_address = self.context_var.resolve(context)

		if email_address is not None:
			character_set = '+-.0123456789@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
			char_list = list(character_set)
			random.shuffle(char_list)

			key = ''.join(char_list)

			cipher_text = ''
			id = 'e' + str(random.randrange(1,999999999))

			for a in email_address:
				cipher_text += key[ character_set.find(a) ]

			script = 'var a="'+key+'";var b=a.split("").sort().join("");var c="'+cipher_text+'";var d="";'
			script += 'for(var e=0;e<c.length;e++)d+=b.charAt(a.indexOf(c.charAt(e)));'
			script += 'document.getElementById("'+id+'").innerHTML="<a class=\\"allcaps darkgreen\\" title=\\""+ d +"\\" href=\\"mailto:"+d+"\\">Email</a>"'

			script = "eval(\""+ script.replace("\\","\\\\").replace('"','\\"') + "\")"
			script = '<script type="text/javascript">/*<![CDATA[*/'+script+'/*]]>*/</script>'

			return '<span id="'+ id + '">[javascript protected email address]</span>'+ script
		return ''


def  encrypt_email(parser, token):
	"""
		{% encrypt_email user.email %}
	"""

	tokens = token.contents.split()
	if len(tokens)!=2:
		raise template.TemplateSyntaxError("%r tag accept two argument" % tokens[0])

	return EncryptEmail(tokens[1])


class EncryptTel(template.Node):

	def __init__(self, context_var):
		self.context_var = template.Variable(context_var)

	def render(self, context):
		import random

		tel = self.context_var.resolve(context)
		character_set = '+-.0123456789'
		char_list = list(character_set)
		random.shuffle(char_list)

		key = ''.join(char_list)

		cipher_text = ''
		id = 't' + str(random.randrange(1,999999999))

		for a in tel:
			cipher_text += key[ character_set.find(a) ]

		script = 'var a="'+key+'";var b=a.split("").sort().join("");var c="'+cipher_text+'";var d="";'
		script += 'for(var e=0;e<c.length;e++)d+=b.charAt(a.indexOf(c.charAt(e)));'
		script += 'document.getElementById("'+id+'").innerHTML="<a class=\\"allcaps darkgreen\\" title=\\""+ d +"\\" href=\\"tel:"+d+"\\">Tel</a>"'

		script = "eval(\""+ script.replace("\\","\\\\").replace('"','\\"') + "\")"
		script = '<script type="text/javascript">/*<![CDATA[*/'+script+'/*]]>*/</script>'

		return '<span id="'+ id + '">[javascript protected phone number]</span>'+ script


def  encrypt_tel(parser, token):
	"""
		{% encrypt_tel user.phone %}
	"""

	tokens = token.contents.split()
	if len(tokens)!=2:
		raise template.TemplateSyntaxError("%r tag accept two argument" % tokens[0])

	return EncryptTel(tokens[1])


class EncryptString(template.Node):

	def __init__(self, context_var):
		self.context_var = template.Variable(context_var)

	def render(self, context):
		import random

		string = self.context_var.resolve(context)
		string = string.replace(' ', '')
		character_set = '+-.0123456789@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
		char_list = list(character_set)
		random.shuffle(char_list)

		key = ''.join(char_list)
		cipher_text = ''
		id = 's' + str(random.randrange(1,999999999))

		for a in string:
			cipher_text += key[character_set.find(a)]

		script = 'var a="' + key + '",b=a.split("").sort().join(""),c="' + cipher_text + '",d="";'
		script += 'for(var e=0;e<c.length;e++)d+=b.charAt(a.indexOf(c.charAt(e)));'
		script += 'document.getElementById("' + id + '").innerHTML=d'
		script = "eval(\""+ script.replace("\\","\\\\").replace('"','\\"') + "\")"
		script = '<script type="text/javascript">/*<![CDATA[*/' + script + '/*]]>*/</script>'

		return '<span id="'+ id + '">[javascript protected]</span>'+ script


def  encrypt_string(parser, token):
	"""
		{% encrypt_string user.phone %}
	"""

	tokens = token.contents.split()
	if len(tokens)!=2:
		raise template.TemplateSyntaxError("%r tag accept two argument" % tokens[0])

	return EncryptString(tokens[1])


register.tag(get_member_info)
register.tag('encrypt_email', encrypt_email)
register.tag('encrypt_tel', encrypt_tel)
register.tag('encrypt_string', encrypt_string)
