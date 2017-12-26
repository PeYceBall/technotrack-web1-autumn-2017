# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from core.models import User
from blog.models import Post
from django.conf import  settings

# Create your models here.


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes')
    post = models.ForeignKey('blog.Post', related_name='likes')