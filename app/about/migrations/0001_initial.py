# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'About'
        db.create_table('about_about', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'About Us', max_length=100, db_index=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=200, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
        ))
        db.send_create_signal('about', ['About'])


    def backwards(self, orm):
        # Deleting model 'About'
        db.delete_table('about_about')


    models = {
        'about.about': {
            'Meta': {'ordering': "('id',)", 'object_name': 'About'},
            'edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'About Us'", 'max_length': '100', 'db_index': 'True'})
        }
    }

    complete_apps = ['about']