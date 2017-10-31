# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import admin
from .models import Post, Blog
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    pass