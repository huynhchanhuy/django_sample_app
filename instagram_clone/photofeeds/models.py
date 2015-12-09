from django.db import models

from PIL import Image as PImage
from instagram_clone.settings import MEDIA_ROOT
from os.path import join as pjoin
from tempfile import NamedTemporaryFile
from string import join
import os
from django.contrib.auth.models import User
from django.core.files import File
#from django_comments.models import Comment
from binascii import hexlify
# class SignUp(models.Model):
# 	pass
	# email = models.EmailField()
	# full_name = models.CharField(max_length=120,default='',blank=True,null=True)
	# timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	# updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	# def __unicode__(self):
	# 	return self.email


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __unicode__(self):
        return self.tag

class Image(models.Model):
    title = models.CharField(max_length=2000, blank=True, null=True)
    image = models.ImageField(upload_to="images/")
    thumbnail = models.ImageField(upload_to="images/", blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User)
    thumbnail2 = models.ImageField(upload_to="images/", blank=True, null=True)
    thumbnail3 = models.ImageField(upload_to="images/", blank=True, null=True)
    imghash = models.CharField(max_length=32, blank=True, null=True)

    def save(self, *args, **kwargs):
        """Save image dimensions."""
        super(Image, self).save(*args, **kwargs)
        im = PImage.open(pjoin(MEDIA_ROOT, self.image.name))
        self.width, self.height = im.size

        self.imghash = hexlify(os.urandom(16))

        # large thumbnail
        fn, ext = os.path.splitext(self.image.name)
        im.thumbnail((1024,768), PImage.ANTIALIAS)
        thumb_fn = fn + "-thumb3" + ext
        tf3 = NamedTemporaryFile()
        im.save(tf3.name, "JPEG")
        self.thumbnail3.save(thumb_fn, File(open(tf3.name)), save=False)
        tf3.close()

        # medium thumbnail
        fn, ext = os.path.splitext(self.image.name)
        im.thumbnail((128,128), PImage.ANTIALIAS)
        thumb_fn = fn + "-thumb2" + ext
        tf2 = NamedTemporaryFile()
        im.save(tf2.name, "JPEG")
        self.thumbnail2.save(thumb_fn, File(open(tf2.name)), save=False)
        tf2.close()

        # small thumbnail
        im.thumbnail((40,40), PImage.ANTIALIAS)
        thumb_fn = fn + "-thumb" + ext
        tf = NamedTemporaryFile()
        im.save(tf.name, "JPEG")
        self.thumbnail.save(thumb_fn, File(open(tf.name)), save=False)
        tf.close()

        super(Image, self).save(*args, **kwargs)

    def size(self):
        """Image size."""
        return "%s x %s" % (self.width, self.height)

    def __unicode__(self):
        return self.imghash

    def tags_(self):
        lst = [x[1] for x in self.tags.values_list()]
        return str(join(lst, ', '))

    def thumbnail_(self):
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" /></a>""" % (
                                                            (self.image.name, self.thumbnail.name))
    thumbnail_.allow_tags = True

class ImageComment(models.Model):
    comment = models.CharField(max_length=2000)
    user = models.ForeignKey(User)
    image = models.ForeignKey(Image)
    created = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.comment

class UserFollow(models.Model):
    user = models.ForeignKey(User, related_name="user_pro5")
    follower = models.ForeignKey(User, related_name="user_follow")
    def __unicode__(self):
        return "UserFollow"

# class ImageComment(models.Model):
#     image = models.ForeignKey(Image, blank=False, null=False)
#     tags = models.ManyToManyField(Tag, blank=True)
#     comment = models.ForeignKey(Comment)
#     created = models.DateTimeField(auto_now_add=True)
#     def tags_(self):
#         lst = [x[1] for x in self.tags.values_list()]
#         return str(join(lst, ', '))
#     def __unicode__(self):
#         return unicode(self.comment)