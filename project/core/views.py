# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from blog.models import Blog
from blog.models import Post
from comment.models import Comment
from .models import User
from django.shortcuts import get_object_or_404
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
    user = get_object_or_404(User.objects.filter(id=request.user.id))
    return render(request, 'profile.html', {'user': user})


class UserDetail(DetailView):
    template_name = 'user.html'
    model = User
    context_object_name = 'user'



# class ProfileView(TemplateView):
#     template_name = 'profile.html'
#     context_object_name = 'this_user'
#
#     def get_context_data(self, **kwargs):
#         context = super(ProfileView, self).get_context_data(**kwargs)
#         return context
