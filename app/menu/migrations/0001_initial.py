# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Menu'
        db.create_table('menu_menu', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
        ))
        db.send_create_signal('menu', ['Menu'])

        # Adding model 'MenuItem'
        db.create_table('menu_menuitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menu.Menu'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['menu.MenuItem'])),
            ('nofollow', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('o', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
        ))
        db.send_create_signal('menu', ['MenuItem'])


    def backwards(self, orm):
        # Deleting model 'Menu'
        db.delete_table('menu_menu')

        # Deleting model 'MenuItem'
        db.delete_table('menu_menuitem')


    models = {
        'menu.menu': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Menu'},
            'edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'menu.menuitem': {
            'Meta': {'ordering': "('o', 'id')", 'object_name': 'MenuItem'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['menu.Menu']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'nofollow': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'o': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['menu.MenuItem']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['menu']