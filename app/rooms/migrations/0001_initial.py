# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Room'
        db.create_table('rooms_room', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('program', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('rooms', ['Room'])


    def backwards(self, orm):
        # Deleting model 'Room'
        db.delete_table('rooms_room')


    models = {
        'rooms.room': {
            'Meta': {'ordering': "('name', 'id')", 'object_name': 'Room'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'program': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rooms']