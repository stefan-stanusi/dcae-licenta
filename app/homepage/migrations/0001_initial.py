# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Info'
        db.create_table('homepage_info', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'Dispozitive, Circuite si Arhitecturi \t\tElectronice', max_length=100, db_index=True)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('anchor_text', self.gf('django.db.models.fields.CharField')(default=u'Citeste mai multe despre noi', max_length=40, blank=True)),
            ('anchor_url', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('bg', self.gf('django.db.models.fields.CharField')(default='#00868b', max_length=30, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('rapid_access', self.gf('django.db.models.fields.CharField')(default='Acces rapid', max_length=100, blank=True)),
            ('study_programs', self.gf('django.db.models.fields.CharField')(default='Programe de studiu', max_length=100, blank=True)),
            ('faculty', self.gf('django.db.models.fields.CharField')(default='Cadre didactice', max_length=100, blank=True)),
            ('resources', self.gf('django.db.models.fields.CharField')(default='Resurse / Suport cursuri', max_length=100, blank=True)),
            ('news', self.gf('django.db.models.fields.CharField')(default='Stiri / noutati', max_length=100, blank=True)),
            ('twitter', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gc', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(default=u'<p>Complex LEU<br>Bd. Iuliu \t\tManiu, nr. 1-3<br>Sect. 6, 061071, Bucuresti, Romania</p>', blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254, blank=True)),
        ))
        db.send_create_signal('homepage', ['Info'])


    def backwards(self, orm):
        # Deleting model 'Info'
        db.delete_table('homepage_info')


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
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'news': ('django.db.models.fields.CharField', [], {'default': "'Stiri / noutati'", 'max_length': '100', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'rapid_access': ('django.db.models.fields.CharField', [], {'default': "'Acces rapid'", 'max_length': '100', 'blank': 'True'}),
            'resources': ('django.db.models.fields.CharField', [], {'default': "'Resurse / Suport cursuri'", 'max_length': '100', 'blank': 'True'}),
            'study_programs': ('django.db.models.fields.CharField', [], {'default': "'Programe de studiu'", 'max_length': '100', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Dispozitive, Circuite si Arhitecturi \\t\\tElectronice'", 'max_length': '100', 'db_index': 'True'}),
            'twitter': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['homepage']