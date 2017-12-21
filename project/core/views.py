# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, CreateView
from blog.models import Blog
from blog.models import Post
from comment.models import Comment
from .models import User
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import resolve
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, get_user_model
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
        context['user'] = self.request.user
        return context


def profile(request):
    user = get_object_or_404(User.objects.filter(id=request.user.id))
    return render(request, 'profile.html', {'user': user})


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


# class RegisterView(CreateView):
#     template_name = 'signup.html'
#     fields = ['username', 'password']
#     model = User
#     success_url = '/'
#
#     def get_context_data(self, **kwargs):
#         context = super(RegisterView, self).get_context_data(**kwargs)
#         if self.request.method == 'post':
#             context['form'] = UserCreationForm(self.request.POST)
#         else:
#             context['form'] = UserCreationForm
#
#         return context
#
#     def form_valid(self, form):
#         form.save()
#         username = form.cleaned_data.get('username')
#         raw_password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password=raw_password)
#         login(self.request, user)
#         return super(RegisterView, self).form_valid(form)


def signup(request):
    user = request.user

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main_page')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'user': user})


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


class LogOutForm:
    pass


class LogOutView:
    pass
