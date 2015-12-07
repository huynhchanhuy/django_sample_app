# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0002_update_user_email_field_length'),
        ('photofeeds', '0002_auto_20151207_0507'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(to='django_comments.Comment', blank=True)),
                ('image', models.ForeignKey(to='photofeeds.Image')),
                ('tags', models.ManyToManyField(to='photofeeds.Tag', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='imagecomments',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='imagecomments',
            name='image',
        ),
        migrations.RemoveField(
            model_name='imagecomments',
            name='tags',
        ),
        migrations.DeleteModel(
            name='ImageComments',
        ),
    ]
