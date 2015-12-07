# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photofeeds', '0003_auto_20151207_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecomment',
            name='comment',
            field=models.ForeignKey(to='django_comments.Comment'),
        ),
    ]
