# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Blog
from blog.models import Post
from comment.models import Comment
# Create your views here.


def main_page(request):
    return render(request, 'main_page.html')


class MainPage(TemplateView):
    template_name = 'main_page.html'
    context_object_name = 'main'

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        context['blogsNumber'] = Blog.objects.all().count()
        context['postsNumber'] = Post.objects.all().count()
        context['commentsNumber'] = Comment.objects.all().count()
        return context


def profile(request):
    return render(request, 'profile.html')