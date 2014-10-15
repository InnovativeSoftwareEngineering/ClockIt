# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('username', models.CharField(error_messages={b'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator(b'^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', b'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('email', models.EmailField(unique=True, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('hire_date', models.DateField(default=django.utils.timezone.now, null=True, blank=True)),
                ('ssn', models.CharField(max_length=9, null=True, blank=True)),
                ('security_level', models.PositiveIntegerField(default=0, choices=[(0, b'User'), (1, b'Manager'), (2, b'Timecard Admin'), (3, b'System Admin')])),
                ('manager', models.ForeignKey(related_name=b'manager_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('address1', models.CharField(max_length=50, null=True, blank=True)),
                ('address2', models.CharField(max_length=50, null=True, blank=True)),
                ('city', models.CharField(max_length=30, null=True, blank=True)),
                ('state', models.CharField(max_length=2, null=True, blank=True)),
                ('phone', models.CharField(max_length=12, null=True, blank=True)),
                ('fax', models.CharField(max_length=12, null=True, blank=True)),
                ('zip_code', models.CharField(max_length=10, null=True, blank=True)),
                ('contact1', models.CharField(max_length=50, null=True, blank=True)),
                ('contact2', models.CharField(max_length=50, null=True, blank=True)),
                ('account_code', models.CharField(max_length=20, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Deliverable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=50)),
                ('group_description', models.CharField(max_length=300, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('default', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(to='timecard.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
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
                ('record_status', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
                ('activity', models.ForeignKey(blank=True, to='timecard.Activity', null=True)),
                ('approved_by', models.ForeignKey(related_name=b'approved_by_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('deliverable', models.ForeignKey(blank=True, to='timecard.Deliverable', null=True)),
                ('project', models.ForeignKey(to='timecard.Project')),
                ('task', models.ForeignKey(blank=True, to='timecard.Task', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='deliverable',
            name='project',
            field=models.ForeignKey(to='timecard.Project'),
            preserve_default=True,
        ),
    ]
