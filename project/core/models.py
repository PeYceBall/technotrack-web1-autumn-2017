# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    description = models.TextField(default='')
