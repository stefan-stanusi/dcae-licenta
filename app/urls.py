from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.template.base import add_to_builtins

import object_tools

from about.views import about
from announcements.views import announcement, announcements, aarchive
from courses.views import course, courses
from homepage.views import homepage
from labs.views import labs, lab
from master.views import masters, master
from members.views import members, member, profile, pty, translate_degrees, \
	translate_experience, translate_activity, \
	translate_notes, transty
from projects.views import projects, project
from publications.views import publications, publication, pubty, \
	edit_publication, pety
from rooms.views import rooms, room
from search.views import search

import datatrans.urls


# Uncomment the next two lines to enable the admin:
from django.contrib import admin

object_tools.autodiscover()
admin.autodiscover()
add_to_builtins('django.templatetags.i18n')
#add_to_builtins('pagination.templatetags.pagination_tags')
add_to_builtins('menu.templatetags.menu_tags')

urlpatterns = i18n_patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^app/', include('app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^i18n/setlang/$', 'django.views.i18n.set_language', name='set_language'),


    url(r'^$', homepage, name='homepage'),
    url(r'^despre/$', about, name='about'),
    ('^pagini/', include('django.contrib.flatpages.urls')),

    url(r'^membri/(?P<pid>\d+)/(?P<slug>.*)/$', member, name='member'),
    url(r'^membri/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^membri/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^membri/$', members, name='members'),

    url(r'^anunturi/(?P<year>\d{4})/(?P<month>\d{2})/$', aarchive, name='aarchive'),
    url(r'^anunturi/(?P<pid>\d+)/(?P<slug>.*)/$', announcement, name='announcement'),
    url(r'^anunturi/$', announcements, name='announcements'),

    url(r'^cursuri/(?P<pid>\d+)/(?P<slug>.*)/$', course, name='course'),
    url(r'^cursuri/$', courses, name='courses'),

    url(r'^laboratoare/(?P<pid>\d+)/(?P<slug>.*)/$', lab, name='lab'),
    url(r'^laboratoare/$', labs, name='labs'),

    url(r'^master/(?P<pid>\d+)/(?P<slug>.*)/$', master, name='master'),
    url(r'^master/$', masters, name='masters'),

    url(r'^proiecte/(?P<pid>\d+)/(?P<slug>.*)/$', project, name='project'),
    url(r'^proiecte/$', projects, name='projects'),

    url(r'^sali/(?P<pid>\d+)/(?P<slug>.*)/$', room, name='room'),
    url(r'^sali/$', rooms, name='rooms'),

    url(r'^publicatii/adauga/$', publication, name='publication'),
    url(r'^publicatii/adauga/ty/$', pubty, name='pubty'),
    url(r'^publicatii/editeaza/(?P<pid>\d+)/$', edit_publication, name='editpublication'),
    url(r'^publicatii/editeaza/ty/$', pety, name='pety'),
    url(r'^publicatii/$', publications, name='publications'),

    url(r'^cautare/$', search, name='search'),

    url(r'^accounts/profile/translate/degrees/$', translate_degrees, name='translate_degrees'),
    url(r'^accounts/profile/translate/experience/$', translate_experience, name='translate_experience'),
    url(r'^accounts/profile/translate/activity/$', translate_activity, name='translate_activity'),
    url(r'^accounts/profile/translate/notes/$', translate_notes, name='translate_notes'),
    url(r'^accounts/profile/translate/ty/$', transty, name='transty'),
    url(r'^accounts/profile/ty/$', pty, name='pty'),
    url(r'^accounts/password/reset/$',  'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/accounts/password/reset/done/', 'from_email': 'noreply@dcae.pub.ro'}, name="password_reset"),
    (r'^accounts/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^accounts/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/accounts/password/done/'}),
    (r'^accounts/password/done/$', 'django.contrib.auth.views.password_reset_complete'),
    url(r'^accounts/profile/$', profile, name='profile'),
)

urlpatterns += patterns('',
    (r'^object-tools/', include(object_tools.tools.urls)),
    (r'^admin/trans/', include(datatrans.urls)),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
