# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20160606_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(to='users.Skill', blank=True),
        ),
    ]
