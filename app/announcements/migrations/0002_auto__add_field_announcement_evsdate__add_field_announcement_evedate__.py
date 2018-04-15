# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Announcement.evsdate'
        db.add_column('announcements_announcement', 'evsdate',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Announcement.evedate'
        db.add_column('announcements_announcement', 'evedate',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Announcement.evlocation'
        db.add_column('announcements_announcement', 'evlocation',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Announcement.evsdate'
        db.delete_column('announcements_announcement', 'evsdate')

        # Deleting field 'Announcement.evedate'
        db.delete_column('announcements_announcement', 'evedate')

        # Deleting field 'Announcement.evlocation'
        db.delete_column('announcements_announcement', 'evlocation')


    models = {
        'announcements.announcement': {
            'Meta': {'ordering': "('-date', '-id')", 'object_name': 'Announcement'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'evedate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'evlocation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'evsdate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'expdate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'blank': 'True'}),
            'img_url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'metadescription': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'noindex': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_index': ('fts.backends.pgsql._VectorField', [], {'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }

    complete_apps = ['announcements']