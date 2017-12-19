# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Blog, Post
# Create your views here.


def blogs_list(request):
    return render(request, 'blogs/blogs_list.html')


def blog(request, blogID):
    return render(request, 'blogs/blog.html', {'blogID': blogID})


def post(request, postID):
    return render(request, 'posts/post.html', {'postID': postID})


class BlogDetail(DetailView):
    template_name = 'blogs/blog.html'
    context_object_name = 'blog'
    model = Blog


class BlogList(ListView):
    template_name = 'blogs/blogs_list.html'
    context_object_name = 'blogs'
    model = Blog


class PostDetail(DetailView):
    template_name = 'posts/post.html'
    context_object_name = 'post'
    model = Post