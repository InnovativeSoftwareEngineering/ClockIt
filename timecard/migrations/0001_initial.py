# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clockit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('begin', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('description', models.TextField(null=True, blank=True)),
                ('activity', models.ForeignKey(to='clockit.Activity')),
                ('deliverable', models.ForeignKey(to='clockit.Deliverable')),
                ('project', models.ForeignKey(to='clockit.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('begin', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('submitted', models.BooleanField(default=False)),
                ('description', models.TextField(null=True, blank=True)),
                ('approved_by', models.ForeignKey(related_name=b'approved_by_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('tasks', models.ManyToManyField(to='timecard.Task')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
