# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 00:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_url', models.CharField(max_length=60)),
                ('note_title', models.CharField(max_length=100)),
                ('note_text', models.CharField(max_length=160)),
                ('note_tags', models.CharField(max_length=150)),
                ('note_timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'note',
            },
        ),
        migrations.CreateModel(
            name='NoteShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sharing_userid', models.CharField(max_length=20)),
                ('shorten_url', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'noteshareobj',
            },
        ),
    ]
