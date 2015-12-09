# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photofeeds', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='email',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='updated',
        ),
    ]
