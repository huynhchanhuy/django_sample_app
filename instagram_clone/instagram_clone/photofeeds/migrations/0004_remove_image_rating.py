# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photofeeds', '0003_auto_20151206_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='rating',
        ),
    ]
