# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def comment(request, commentID):

    return render(request, 'comments/comment.html', {'commentID' : commentID})