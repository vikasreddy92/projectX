# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-07 20:39
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
            name='TJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=50)),
                ('appliedOn', models.DateField(help_text='Please use the following format:  YYYY-MM-DD')),
                ('source', models.CharField(max_length=50)),
                ('jobId', models.CharField(blank=True, max_length=50)),
                ('jobDesc', models.CharField(blank=True, max_length=200)),
                ('statusLink', models.URLField(blank=True)),
                ('result', models.CharField(choices=[('A', 'accept'), ('R', 'reject'), ('U', 'unknown')], default='U', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
