# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    fieldsets = BaseUserAdmin.fieldsets + (
        (u'Дополнительно', {'fields': ('admin_avatar', 'avatar')}),
    )
    readonly_fields = ('admin_avatar', )

    def admin_avatar(self, instance):
        return instance.avatar and u'<img src="{0}" width="100px" />'.format(
            instance.avatar.url
        )
    admin_avatar.allow_tags = True
    admin_avatar.short_description = u'Аватар'

