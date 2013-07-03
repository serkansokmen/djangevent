# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Session'
        db.create_table(u'events_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'events', ['Session'])

        # Adding M2M table for field sessions on 'Event'
        m2m_table_name = db.shorten_name(u'events_event_sessions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'events.event'], null=False)),
            ('session', models.ForeignKey(orm[u'events.session'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'session_id'])


    def backwards(self, orm):
        # Deleting model 'Session'
        db.delete_table(u'events_session')

        # Removing M2M table for field sessions on 'Event'
        db.delete_table(db.shorten_name(u'events_event_sessions'))


    models = {
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sessions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['events.Session']", 'symmetrical': 'False'}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        u'events.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'events.session': {
            'Meta': {'object_name': 'Session'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['events']