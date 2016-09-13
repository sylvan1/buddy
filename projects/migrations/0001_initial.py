# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20160613_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Name of the project')),
                ('description', models.TextField()),
                ('expiration_date', models.DateField()),
                ('number_of_users_required', models.PositiveSmallIntegerField()),
                ('opensource', models.BooleanField()),
                ('url', models.URLField()),
                ('slug', models.SlugField(unique=True)),
                ('i_want_to_join', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
                ('owner', models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('skills', models.ManyToManyField(to='users.Skill', blank=True)),
                ('users', models.ManyToManyField(related_name='member', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
    ]
