# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Programme'
        db.create_table('master_programme', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('search_index', self.gf('fts.backends.pgsql._VectorField')(null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('studies', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('master', ['Programme'])

        # Adding M2M table for field partners on 'Programme'
        db.create_table('master_programme_partners', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('programme', models.ForeignKey(orm['master.programme'], null=False)),
            ('partner', models.ForeignKey(orm['partners.partner'], null=False))
        ))
        db.create_unique('master_programme_partners', ['programme_id', 'partner_id'])


    def backwards(self, orm):
        # Deleting model 'Programme'
        db.delete_table('master_programme')

        # Removing M2M table for field partners on 'Programme'
        db.delete_table('master_programme_partners')


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
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'})
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