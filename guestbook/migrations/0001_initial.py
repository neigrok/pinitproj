# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-25 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'guestbook_commentary',
            },
        ),
    ]
