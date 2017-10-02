# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def main_page(request):
    return render(request, 'main_page.html')


def blogs_list(request):
    return render(request, 'blogs_list.html')


def blog(request, blogID):
    return render(request, 'blog.html', {'blogID': blogID})


def post(request, blogID, postID):
    return render(request, 'post.html', {'blogID': blogID, 'postID': postID})


def profile(request):
    return render(request, 'profile.html')