# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0002_update_user_email_field_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photofeeds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'images/')),
                ('thumbnail', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('width', models.IntegerField(null=True, blank=True)),
                ('height', models.IntegerField(null=True, blank=True)),
                ('thumbnail2', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('thumbnail3', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(to='django_comments.Comment', blank=True)),
                ('image', models.ForeignKey(to='photofeeds.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='SignUp',
        ),
        migrations.AddField(
            model_name='imagecomments',
            name='tags',
            field=models.ManyToManyField(to='photofeeds.Tag', blank=True),
        ),
    ]
