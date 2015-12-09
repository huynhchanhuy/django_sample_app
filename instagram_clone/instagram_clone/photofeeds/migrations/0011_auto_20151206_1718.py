# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photofeeds', '0010_remove_comment_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='image',
            name='height',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.RemoveField(
            model_name='image',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='image',
            name='thumbnail2',
        ),
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
        migrations.RemoveField(
            model_name='image',
            name='width',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tag',
        ),
    ]
