# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Info.image_ro'
        db.add_column('homepage_info', 'image_ro',
                      self.gf('django.db.models.fields.files.ImageField')(default='/static/img/home_lead.jpg', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Info.logo_ro'
        db.add_column('homepage_info', 'logo_ro',
                      self.gf('django.db.models.fields.files.ImageField')(default='/static/img/home_logos.png', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Info.image_ro'
        db.delete_column('homepage_info', 'image_ro')

        # Deleting field 'Info.logo_ro'
        db.delete_column('homepage_info', 'logo_ro')


    models = {
        'homepage.info': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Info'},
            'address': ('django.db.models.fields.TextField', [], {'default': "u'<p>Complex LEU<br>Bd. Iuliu \\t\\tManiu, nr. 1-3<br>Sect. 6, 061071, Bucuresti, Romania</p>'", 'blank': 'True'}),
            'anchor_text': ('django.db.models.fields.CharField', [], {'default': "u'Citeste mai multe despre noi'", 'max_length': '40', 'blank': 'True'}),
            'anchor_url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'bg': ('django.db.models.fields.CharField', [], {'default': "'#00868b'", 'max_length': '30', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'faculty': ('django.db.models.fields.CharField', [], {'default': "'Cadre didactice'", 'max_length': '100', 'blank': 'True'}),
            'gc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'image_ro': ('django.db.models.fields.files.ImageField', [], {'default': "'/static/img/home_lead.jpg'", 'max_length': '100', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'logo_ro': ('django.db.models.fields.files.ImageField', [], {'default': "'/static/img/home_logos.png'", 'max_length': '100', 'blank': 'True'}),
            'news': ('django.db.models.fields.CharField', [], {'default': "'Stiri / noutati'", 'max_length': '100', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'rapid_access': ('django.db.models.fields.CharField', [], {'default': "'Acces rapid'", 'max_length': '100', 'blank': 'True'}),
            'resources': ('django.db.models.fields.CharField', [], {'default': "'Resurse / Suport cursuri'", 'max_length': '100', 'blank': 'True'}),
            'study_programs': ('django.db.models.fields.CharField', [], {'default': "'Programe de studiu'", 'max_length': '100', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Dispozitive, Circuite si Arhitecturi Electronice'", 'max_length': '100', 'db_index': 'True'}),
            'twitter': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['homepage']