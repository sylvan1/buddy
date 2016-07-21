# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='programming_lang',
            field=models.CharField(unique=True, max_length=255, verbose_name='language'),
        ),
    ]
