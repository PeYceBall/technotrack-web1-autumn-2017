# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.views import View
from django import forms
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blog, Post
from comment.models import Comment
# Create your views here.


def blogs_list(request):
    return render(request, 'blogs/blogs_list.html')


def blog(request, blogID):
    return render(request, 'blogs/blog.html', {'blogID': blogID})


def post(request, postID):
    return render(request, 'posts/post.html', {'postID': postID})


class PostUpdate(UpdateView):
    template_name = 'posts/edit_post.html'
    context_object_name = 'post'
    model = Post

    fields = ['title', 'text']

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['post'] = self.get_object()
        context['text_initial'] = self.get_object().text
        context['title_initial'] = self.get_object().title

        if self.request.method == 'post':
            context['form'] = PostForm(self.request.POST)
        else:
            form = PostForm()
            form.fields['text'].initial = self.get_object().text
            form.fields['title'].initial = self.get_object().title
            context['form'] = form

        return context

    def form_valid(self, form):

        self.success_url = reverse('blog:post_detail', kwargs={'pk': self.kwargs['pk'], 'blog_id': self.get_object().id})
        return super(PostUpdate, self).form_valid(form)


class PostCreate(CreateView):
    template_name = 'posts/new_post.html'
    context_object_name = 'post'
    model = Post

    fields = ['title', 'text']

    def get_context_data(self, **kwargs):
        context = super(PostCreate, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['blog'] = Blog.objects.get(pk=self.kwargs['pk'])

        if self.request.method == 'post':
            context['form'] = PostForm(self.request.POST)
        else:
            context['form'] = PostForm()

        return context

    def form_valid(self, form):
        self.success_url = reverse('blog:blog_detail', kwargs={'pk': self.kwargs['pk'], 'blog_id': self.get_object().id})
        form.instance.blog = Blog.objects.get(pk=self.kwargs['pk'])
        return super(PostCreate, self).form_valid(form)


class BlogDetail(DetailView):
    template_name = 'blogs/blog.html'
    context_object_name = 'blog'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class BlogList(CreateView, ListView):
    template_name = 'blogs/blogs_list.html'
    context_object_name = 'blogs'
    model = Blog
    paginate_by = 11
    fields = ['title']

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['user'] = self.request.user

        if self.request.method == 'post':
            context['form'] = BlogForm(self.request.POST)
        else:
            blog_list = self.get_queryset()
            paginator = Paginator(blog_list, 15)
            page = self.request.GET.get('page')
            try:
                blogs_page = paginator.page(page)
            except PageNotAnInteger:
                blogs_page = paginator.page(1)
            except EmptyPage:
                blogs_page = paginator.page(paginator.num_pages)

            context['blogs_page'] = blogs_page
            context['form'] = BlogForm()

        context['sort_form'] = self.sort_form
        return context

    def form_valid(self, form):

        form.instance.owner = self.request.user
        form.instance.title = form.cleaned_data['title']
        form.save()
        return redirect('blog:blog_detail', pk=form.instance.id)

    def get_queryset(self):
        query_set = super(BlogList, self).get_queryset()
        self.sort_form = BlogSortForm(self.request.GET)


        if self.sort_form.is_valid():
            print "WOW"
            if self.sort_form.cleaned_data['order_by']:
                query_set = query_set.order_by(self.sort_form.cleaned_data['order_by'])
            if self.sort_form.cleaned_data['search']:
                query_set = query_set.filter(title=self.sort_form.cleaned_data['search'])

        return query_set


class PostDetail(DetailView, CreateView):
    template_name = 'posts/post.html'
    context_object_name = 'post'
    model = Post

    fields = ['text']

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['user'] = self.request.user

        if self.request.method == 'post':
            context['form'] = CommentForm(self.request.POST)
        else:
            context['form'] = CommentForm()

        return context

    def form_valid(self, form):
        self.success_url = self.request.path
        comment = Comment()
        comment.author = self.request.user
        comment.post = self.get_object()
        comment.text = form.cleaned_data['text']
        comment.save()

        return redirect(self.success_url)


class BlogForm(forms.Form):
    title = forms.CharField()


class BlogSortForm(forms.Form):
    search = forms.CharField(required=False)
    order_by = forms.ChoiceField(choices=(
        ('title', 'Название ↓'),
        ('-title', 'Название ↑'),
        ('id', 'ID')
    ), required=False)


class PostForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
