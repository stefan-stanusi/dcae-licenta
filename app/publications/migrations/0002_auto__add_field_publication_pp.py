# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Publication.pp'
        db.add_column('publications_publication', 'pp',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Publication.pp'
        db.delete_column('publications_publication', 'pp')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'members.member': {
            'Meta': {'ordering': "('name', 'id')", 'object_name': 'Member'},
            'activity': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'alumnus': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'coord_bachelor': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'coord_bachelor_rel_+'", 'null': 'True', 'to': "orm['members.Member']"}),
            'coord_msc': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'coord_msc_rel_+'", 'null': 'True', 'to': "orm['members.Member']"}),
            'coord_phd': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'coord_phd_rel_+'", 'null': 'True', 'to': "orm['members.Member']"}),
            'coordinator': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'coordinator_rel_+'", 'null': 'True', 'to': "orm['members.Member']"}),
            'degrees': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'experience': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'faculty': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'blank': 'True'}),
            'img_url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'r': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'members'", 'to': "orm['members.Role']"}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'search_index': ('fts.backends.pgsql._VectorField', [], {'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'u': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': "orm['auth.User']", 'unique': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'members.role': {
            'Meta': {'ordering': "('o', 'id')", 'object_name': 'Role'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'o': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'singular_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'publications.genre': {
            'Meta': {'ordering': "('name', 'id')", 'object_name': 'Genre'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'publications.publication': {
            'Meta': {'ordering': "('year', 'title')", 'object_name': 'Publication'},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['members.Member']", 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'conference': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gen': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['publications.Genre']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oauthors': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'other': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pp': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'review': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'search_index': ('fts.backends.pgsql._VectorField', [], {'null': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'year': ('django.db.models.fields.SmallIntegerField', [], {'max_length': '4'})
        }
    }

    complete_apps = ['publications']