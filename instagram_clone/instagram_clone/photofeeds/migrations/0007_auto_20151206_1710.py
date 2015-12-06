# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('photofeeds', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='thumbnail3',
            field=models.ImageField(null=True, upload_to=b'images/', blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ForeignKey(default=datetime.datetime(2015, 12, 6, 17, 9, 54, 855876, tzinfo=utc), to='photofeeds.Image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=datetime.datetime(2015, 12, 6, 17, 10, 4, 248416, tzinfo=utc), to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
