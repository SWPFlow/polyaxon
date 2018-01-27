# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-27 15:20
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import libs.blacklist
import libs.spec_validation
import re
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperimentGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('sequence', models.IntegerField(editable=False, help_text='The sequence number of this group within the project.')),
                ('content', models.TextField(help_text='The yaml content of the polyaxonfile/specification.', validators=[libs.spec_validation.validate_spec_content])),
            ],
            options={
                'ordering': ['sequence'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z', 32), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid'), libs.blacklist.validate_blacklist_name])),
                ('is_public', models.BooleanField(default=True, help_text='If project is public or private.')),
                ('has_tensorboard', models.BooleanField(default=False, help_text='If project has a tensorboard.')),
                ('has_notebook', models.BooleanField(default=False, help_text='If project has a notebook.')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='experimentgroup',
            name='project',
            field=models.ForeignKey(help_text='The project this polyaxonfile belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='experiment_groups', to='projects.Project'),
        ),
        migrations.AddField(
            model_name='experimentgroup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiment_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('user', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='experimentgroup',
            unique_together=set([('project', 'sequence')]),
        ),
    ]
