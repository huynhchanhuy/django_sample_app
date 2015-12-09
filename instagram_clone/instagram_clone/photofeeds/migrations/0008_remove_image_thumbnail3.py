# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photofeeds', '0007_auto_20151206_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='thumbnail3',
        ),
    ]
