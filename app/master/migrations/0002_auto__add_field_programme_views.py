# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Programme.views'
        db.add_column('master_programme', 'views',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Programme.views'
        db.delete_column('master_programme', 'views')


    models = {
        'master.programme': {
            'Meta': {'ordering': "('name', 'id')", 'object_name': 'Programme'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['partners.Partner']", 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_index': ('fts.backends.pgsql._VectorField', [], {'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'studies': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
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

    complete_apps = ['master']