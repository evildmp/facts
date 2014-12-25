# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fact'
        db.create_table('facts_fact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=316)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 12, 25, 0, 0))),
        ))
        db.send_create_signal('facts', ['Fact'])


    def backwards(self, orm):
        # Deleting model 'Fact'
        db.delete_table('facts_fact')


    models = {
        'facts.fact': {
            'Meta': {'ordering': "['timestamp']", 'object_name': 'Fact'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '316'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 25, 0, 0)'})
        }
    }

    complete_apps = ['facts']