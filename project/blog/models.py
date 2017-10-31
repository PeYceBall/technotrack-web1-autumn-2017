# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

class Post(models.Model):
    blog = models.ForeignKey('blog.Blog', related_name='posts')
    title = models.CharField(max_length=255, default='')
    text = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

