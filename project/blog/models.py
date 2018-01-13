# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255, default='')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blogs')

    def __unicode__(self):
        return self.title


class Post(models.Model):
    blog = models.ForeignKey('blog.Blog', related_name='posts')
    title = models.CharField(max_length=255, default='')
    text = models.TextField(default='')
    categories = models.ManyToManyField('category.Category', related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
