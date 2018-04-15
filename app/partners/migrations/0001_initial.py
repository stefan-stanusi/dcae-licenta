# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Partner'
        db.create_table('partners_partner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('o', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
        ))
        db.send_create_signal('partners', ['Partner'])


    def backwards(self, orm):
        # Deleting model 'Partner'
        db.delete_table('partners_partner')


    models = {
        'partners.partner': {
            'Meta': {'ordering': "('o', 'id')", 'object_name': 'Partner'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'o': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['partners']